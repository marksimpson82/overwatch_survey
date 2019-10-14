#!/bin/bash
readonly script_name=${0##*/}

function run_failure {
   echo "FAILED AT $script_name:$1"
   exit 1
}

trap 'run_failure $LINENO' ERR
set -eu

(cd overwatch_survey && python transform_data.py)

readonly tmp_dir=$(mktemp -d)

# convert notebook => markdown (though it'll still contain python code atm)
jupyter nbconvert --to markdown overwatch_survey/Analysis.ipynb --output-dir "static_site"

# we strip out the python code to finalise things afterwards
(cd overwatch_survey && python static_site_prep.py)

(cd static_site && bundle exec jekyll serve)

# Overwatch Survey Analysis

## Pre-requisites
Tested with Python 3.7.4, but earlier versions of Python3 should work.

## Install & create virtualenv shell 
```bash
$ pip install --user hatch
$ hatch shell
$ hatch install
```

## Preparing the data
The format of the google sheets survey results isn't great for using it with pandas/notebook etc. Transform it into a form that's more suitable for visualising the results.

```bash
$ python transform_data.py
```

## Running the notebook
```bash
$ jupyter notebook
```

This will start a local server, and launch a browser tab pointing at http://localhost:8888/notebooks/

## Exporting to Markdown
**Note**: While you can export to HTML via `--to html`, nbconvert exports a bloated page with unused CSS & base64-encoded images. It took the page from ~250KB to over 700KB! Instead, we export to Markdown, then build a static page using [Jekyll](https://jekyllrb.com/).

In the activated hatch shell:

`$ jupyter nbconvert --to markdown overwatch_survey\Analysis.ipynb --output-dir static_site`

### Remove the python code from the Markdown
While it should be possible to write a template that does this in the above `nbconvert` step, I couldn't get it working. Instead, run: 

`$ python static_site_prep.py`

## Building the HTML page
Install [Jekyll](https://jekyllrb.com/) (note: it's a bit of a pain if you want to install it [on Windows](https://jekyllrb.com/docs/installation/windows/))

Then run:

```bash
$ cd static_site
$ bundle exec jekyll serve
```

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

## Exporting to HTML
We could use nbconvert with some templating/extensions, but this quick & dirty hack will do for now.

In the activated hatch shell, follow the steps from this [stackoverflow answer](https://stackoverflow.com/a/49269085/83891):

* `$ ipython nbconvert --to html overwatch_survey\Analysis.ipynb` 
* Open `Analysis.html` in a browser
* Open the console (via F12 -> Console)
* paste & run: `document.querySelectorAll("div.input").forEach(function(a){a.remove()})`
* Save page as HTML



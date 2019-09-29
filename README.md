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

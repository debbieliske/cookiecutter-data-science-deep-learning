# Cookiecutter Data Science for Deep Learning and MLFlow

_"A logical, reasonably standardized, but flexible project structure for doing and sharing data science work..." specific to Deep
Learning (or Machine Learning). This cookiecutter is initially based on cookie-cutter-data-science and is extended to set up skeleton code for deep learning projects._

This cookiecutter utilizes tensorflow, Keras, MLFlow and Dask as it's core functionality. By default, it installs the following in the pipfile:

numpy, pandas, [mlflow](http://mlflow.org), [tensorflow](http://tensorflow.org), [keras](http://keras.io), [dask_ml](http://dask.org), [dask](http://dask.org), atomicwrites (an internal utility), awscli, fastparquet (for using Parquet data containers)

Dask provides advanced parallelism for analytics, enabling performance at scale. ML Flow is an open source platform for the machine learning lifecycle. Keras is an API that is a central part of the TensorFlow 2.0 ecosystem, covering all of the machine learning workflow.

After running this cookiecutter, you will have auto-generated deep learning feature, train, and predict python files with skeleton code to get you started with the tools listed above (including a local atomic write utility). Please see the resulting directory structure below.

#### [Project homepage](http://github.com/debbieliske/cookiecutter-data-science-deep-learning/)



### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/drivendata/cookiecutter-data-science-deep-learning



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
|   |       
|   |__ utils          <- Scripts to perform random utility functionality
|   |   |
|   |   |__ atomic_write.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests

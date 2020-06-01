# Team13: Capstone project of Python Bootcamp

## Purpose

State the purpose of the notebook.

## Methology

Quickly describe assumptions and processing steps.

## Improvements

* Find a dataset that has at least 2 CSV files
* Come up with 5 questions that you want to answer while exploring the dataset
* Perform EDA (Exploratoty Data Analysis) on your dataset with basic visualisations

## Results

## Setup


```python
# install system dependencies
import os

!conda install -c conda-forge --yes pandas jupyterthemes seaborn jupyter_contrib_nbextensions pandoc
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    # All requested packages already installed.
    


### Library Import


```python
# load libraries and setup environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)
```

## Parameter definition

We set all relevant parameters for our notebook. By convention, parameters are uppercase, while all the other variables follow Python's guidelines.

## Data import
We retrieve all the required data for the analysis.

## Data processing
Put here the core of the notebook. Feel free di further split this section into subsections.

## References

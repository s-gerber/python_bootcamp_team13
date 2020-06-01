#!/usr/bin/env python
# coding: utf-8

# # Team13: Capstone project of Python Bootcamp
# 
# ## Purpose
# 
# State the purpose of the notebook.
# 
# ## Methology
# 
# Quickly describe assumptions and processing steps.
# 
# ## TODO / Improvements
# 
# * [x] Find a dataset that has at least 2 CSV files
# * [ ] Come up with 5 questions that you want to answer while exploring the dataset
# * [ ] Perform EDA (Exploratoty Data Analysis) on your dataset with basic visualisations
# 
# ## Results
# 
# ## Setup

# In[3]:


# install system dependencies
import os

get_ipython().system('conda install -c conda-forge --yes pandas jupyterthemes seaborn jupyter_contrib_nbextensions pandoc')


# ### Library Import

# In[7]:


# load libraries and setup environment
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)


# ## Parameter definition
# 
# We set all relevant parameters for our notebook. By convention, parameters are uppercase, while all the other variables follow Python's guidelines.
# 
# ## Data import
# We retrieve all the required data for the analysis.
# 
# ## Data processing
# Put here the core of the notebook. Feel free di further split this section into subsections.
# 
# ## References
# 
# * [data for the cost of living](https://www.kaggle.com/andytran11996/cost-of-living/)
# * [base data for countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world)
# * [data for life expectancy from the WHO](https://www.kaggle.com/kumarajarshi/life-expectancy-who)
# * [roshansharma_europe-datasets](https://www.kaggle.com/roshansharma/europe-datasets)

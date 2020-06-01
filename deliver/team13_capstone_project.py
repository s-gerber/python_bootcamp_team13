#!/usr/bin/env python
# coding: utf-8

# # Team13: Capstone project of Python Bootcamp
# 
# This is [the Capstone project for Team 13 of the Python Data Analysis Bootcamp](https://github.com/pyladiesams/Bootcamp-Data-Analysis-beginner-apr-may2020/blob/master/Capstone/README.md).
# We are trying, more or less, to follow the structure of [jupytemplate](https://github.com/xtreamsrl/jupytemplate/blob/master/jupytemplate/jupytemplate/template.ipynb).
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

# In[16]:


# install system dependencies
import sys
import os

get_ipython().system('conda install -c conda-forge --yes --prefix {sys.prefix} pandas jupyterthemes seaborn jupyter_contrib_nbextensions pandoc')


# ### Library Import

# In[96]:


# load libraries and setup environment
# mandatory
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

# optional
import numpy as np
import seaborn as sns
from jupyterthemes import jtplot
from IPython.core.display import HTML
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)


# ## Parameter definition
# 
# We set all relevant parameters for our notebook. By convention, parameters are uppercase, while all the other variables follow Python's guidelines.
# 
# ## Data import
# We retrieve all the required data for the analysis.

# In[83]:


cost_of_living = pd.read_csv('../data/andytran11996_cost-of-living/datasets_73059_162758_cost-of-living-2018.csv')

# we are droppping the Rank column because it's entirely empty
cost_of_living = cost_of_living.drop(columns = 'Rank')


# ## Data processing
# 
# ### 1. What are the five cities with the highest/lowest cost of living (incl. rent)?

# In[153]:


caption_column = 'City'
index_column = 'Cost of Living Plus Rent Index'

def display_cost_of_living(costs, title):
    filtered_costs = costs[[caption_column, index_column]].sort_values(index_column)
    filtered_costs.plot.barh(title = title, x = caption_column, y = index_column)
    plt.show()
    display(filtered_costs.style.hide_index())

# print the ten most expensive cities in the database in 2018
display_cost_of_living(cost_of_living.nlargest(5, index_column), 'Largest Rent Index')
display_cost_of_living(cost_of_living.nsmallest(5, index_column), 'Smallest Rent Index')


# ## References
# 
# * [data for the cost of living](https://www.kaggle.com/andytran11996/cost-of-living/)
# * [base data for countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world)
# * [data for life expectancy from the WHO](https://www.kaggle.com/kumarajarshi/life-expectancy-who)
# * [roshansharma_europe-datasets](https://www.kaggle.com/roshansharma/europe-datasets)

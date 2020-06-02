# Team13: Capstone project of Python Bootcamp

This is [the Capstone project for Team 13 of the Python Data Analysis Bootcamp](https://github.com/pyladiesams/Bootcamp-Data-Analysis-beginner-apr-may2020/blob/master/Capstone/README.md).
We are trying, more or less, to follow the structure of [jupytemplate](https://github.com/xtreamsrl/jupytemplate/blob/master/jupytemplate/jupytemplate/template.ipynb).

## Purpose

State the purpose of the notebook.

## Methology

Quickly describe assumptions and processing steps.

## TODO / Improvements

* [x] Find a dataset that has at least 2 CSV files
* [ ] Come up with 5 questions that you want to answer while exploring the dataset
* [ ] Perform EDA (Exploratoty Data Analysis) on your dataset with basic visualisations

## Results

## Setup


```python
# install system dependencies
import sys
import os

!conda install -c conda-forge --yes --prefix {sys.prefix} pandas jupyterthemes seaborn jupyter_contrib_nbextensions pandoc
```

    Collecting package metadata (current_repodata.json): done
    Solving environment: done
    
    # All requested packages already installed.
    


### Library Import


```python
# load libraries and setup environment
# mandatory
import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt

# optional
import numpy as np
import seaborn as sns
from jupyterthemes import jtplot
from IPython.core.display import HTML
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)
```

## Parameter definition

We set all relevant parameters for our notebook. By convention, parameters are uppercase, while all the other variables follow Python's guidelines.


```python
COAST_COLUMN = "Coastline (coast/area ratio)"
COUNTRY_COLUMN = 'Country'
SATISFACTION_COLUMN = "People with highest life satisfaction [%]"
```

## Data import
We retrieve all the required data for the analysis.


```python
cost_of_living = pd.read_csv('../data/andytran11996_cost-of-living/datasets_73059_162758_cost-of-living-2018.csv')

# we are droppping the Rank column because it's entirely empty
cost_of_living = cost_of_living.drop(columns = 'Rank')

life_satisfaction = pd.read_csv('../data/roshansharma_europe-datasets/datasets_231225_493692_life_satisfaction_2013.csv')
life_satisfaction = life_satisfaction.rename(columns = { "prct_life_satis_high": "People with highest life satisfaction [%]", "country": "Country" })
life_satisfaction['Country'] = life_satisfaction['Country'].astype(str)
life_satisfaction['Country'] = life_satisfaction['Country'].str.strip()

generic_country_data = pd.read_csv('../data/fernandol_countries-of-the-world/datasets_23752_30346_countries of the world.csv', decimal=',')
generic_country_data['Country'] = generic_country_data['Country'].astype(str)
generic_country_data['Country'] = generic_country_data['Country'].str.strip()
generic_european_country_data = generic_country_data[generic_country_data['Region'].str.contains('EUROPE', case = False)]

print('successfully imported the datasets.')
```

    successfully imported the datasets.


## Data processing

### 1. What are the five cities with the highest/lowest cost of living (incl. rent)?


```python
caption_column = 'City'
index_column = 'Cost of Living Plus Rent Index'

def display_cost_of_living(costs, title):
    filtered_costs = costs[[caption_column, index_column]].sort_values(index_column, ascending = True)
    filtered_costs.plot.barh(title = title, x = caption_column, y = index_column)
    plt.show();
    display(filtered_costs.sort_values(index_column, ascending = False).style.hide_index())

# print the ten most expensive cities in the database in 2018
display_cost_of_living(cost_of_living.nlargest(5, index_column), 'Largest Rent Index')
display_cost_of_living(cost_of_living.nsmallest(5, index_column), 'Smallest Rent Index')
```


![png](team13_capstone_project_files/team13_capstone_project_10_0.png)



<style  type="text/css" >
</style><table id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3" ><thead>    <tr>        <th class="col_heading level0 col0" >City</th>        <th class="col_heading level0 col1" >Cost of Living Plus Rent Index</th>    </tr></thead><tbody>
                <tr>
                                <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row0_col0" class="data row0 col0" >Hamilton, Bermuda</td>
                        <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row0_col1" class="data row0 col1" >128.760000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row1_col0" class="data row1 col0" >San Francisco, CA, United States</td>
                        <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row1_col1" class="data row1 col1" >106.290000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row2_col0" class="data row2 col0" >Zurich, Switzerland</td>
                        <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row2_col1" class="data row2 col1" >105.030000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row3_col0" class="data row3 col0" >Geneva, Switzerland</td>
                        <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row3_col1" class="data row3 col1" >104.380000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row4_col0" class="data row4 col0" >New York, NY, United States</td>
                        <td id="T_a52d3ac8_a4ee_11ea_9865_2df6e64f41b3row4_col1" class="data row4 col1" >100.000000</td>
            </tr>
    </tbody></table>



![png](team13_capstone_project_files/team13_capstone_project_10_2.png)



<style  type="text/css" >
</style><table id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3" ><thead>    <tr>        <th class="col_heading level0 col0" >City</th>        <th class="col_heading level0 col1" >Cost of Living Plus Rent Index</th>    </tr></thead><tbody>
                <tr>
                                <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row0_col0" class="data row0 col0" >Bhubaneswar, India</td>
                        <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row0_col1" class="data row0 col1" >15.140000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row1_col0" class="data row1 col0" >Visakhapatnam, India</td>
                        <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row1_col1" class="data row1 col1" >15.110000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row2_col0" class="data row2 col0" >Mysore, India</td>
                        <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row2_col1" class="data row2 col1" >14.980000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row3_col0" class="data row3 col0" >Alexandria, Egypt</td>
                        <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row3_col1" class="data row3 col1" >14.400000</td>
            </tr>
            <tr>
                                <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row4_col0" class="data row4 col0" >Thiruvananthapuram, India</td>
                        <td id="T_a52d3ac9_a4ee_11ea_9865_2df6e64f41b3row4_col1" class="data row4 col1" >13.260000</td>
            </tr>
    </tbody></table>


## 2. What are the five happiest countries in Europe?


```python
index_column = "People with highest life satisfaction [%]"
caption_column = 'Country'

top_countries_life_satisfaction = life_satisfaction[[caption_column, index_column]]
top_countries_life_satisfaction = top_countries_life_satisfaction.nlargest(5, index_column)
top_countries_life_satisfaction = top_countries_life_satisfaction.sort_values(index_column, ascending = True)
top_countries_life_satisfaction.plot.barh(title = 'Percentage of satisfied people', x = caption_column, y = index_column);
plt.show();
display(top_countries_life_satisfaction.sort_values(index_column, ascending = False).style.hide_index())
```


![png](team13_capstone_project_files/team13_capstone_project_12_0.png)



<style  type="text/css" >
</style><table id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3" ><thead>    <tr>        <th class="col_heading level0 col0" >Country</th>        <th class="col_heading level0 col1" >People with highest life satisfaction [%]</th>    </tr></thead><tbody>
                <tr>
                                <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row0_col0" class="data row0 col0" >Denmark</td>
                        <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row0_col1" class="data row0 col1" >42.700000</td>
            </tr>
            <tr>
                                <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row1_col0" class="data row1 col0" >Finland</td>
                        <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row1_col1" class="data row1 col1" >38.600000</td>
            </tr>
            <tr>
                                <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row2_col0" class="data row2 col0" >Switzerland</td>
                        <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row2_col1" class="data row2 col1" >38.500000</td>
            </tr>
            <tr>
                                <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row3_col0" class="data row3 col0" >Iceland</td>
                        <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row3_col1" class="data row3 col1" >38.100000</td>
            </tr>
            <tr>
                                <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row4_col0" class="data row4 col0" >Austria</td>
                        <td id="T_a52d3aca_a4ee_11ea_9865_2df6e64f41b3row4_col1" class="data row4 col1" >37.900000</td>
            </tr>
    </tbody></table>


## 3. What are the European countries with the most coast line in relation to their area?


```python
index_column = "Coastline (coast/area ratio)"
caption_column = 'Country'

coastline_data = generic_european_country_data[[caption_column, index_column]]

coastline_data = coastline_data.nlargest(5, index_column)
coastline_data = coastline_data.sort_values(index_column, ascending = True)
coastline_data.plot.barh(title = 'Countries with the most coast line in relation to their area', x = caption_column, y = index_column);
plt.show();
display(coastline_data.sort_values(index_column, ascending = False).style.hide_index())
```


![png](team13_capstone_project_files/team13_capstone_project_14_0.png)



<style  type="text/css" >
</style><table id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3" ><thead>    <tr>        <th class="col_heading level0 col0" >Country</th>        <th class="col_heading level0 col1" >Coastline (coast/area ratio)</th>    </tr></thead><tbody>
                <tr>
                                <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row0_col0" class="data row0 col0" >Monaco</td>
                        <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row0_col1" class="data row0 col1" >205.000000</td>
            </tr>
            <tr>
                                <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row1_col0" class="data row1 col0" >Gibraltar</td>
                        <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row1_col1" class="data row1 col1" >171.430000</td>
            </tr>
            <tr>
                                <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row2_col0" class="data row2 col0" >Faroe Islands</td>
                        <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row2_col1" class="data row2 col1" >79.840000</td>
            </tr>
            <tr>
                                <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row3_col0" class="data row3 col0" >Guernsey</td>
                        <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row3_col1" class="data row3 col1" >64.100000</td>
            </tr>
            <tr>
                                <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row4_col0" class="data row4 col0" >Malta</td>
                        <td id="T_a52d3acb_a4ee_11ea_9865_2df6e64f41b3row4_col1" class="data row4 col1" >62.280000</td>
            </tr>
    </tbody></table>


## 4. Is there a correlation between happiness and access to a coastline?


```python
merged = pd.merge(generic_european_country_data, life_satisfaction, on = COUNTRY_COLUMN, how = 'inner')  

coastline_data = generic_european_country_data[[COAST_COLUMN, COUNTRY_COLUMN]]

# sort by coast
merged = merged.sort_values(COAST_COLUMN, ascending = True, ignore_index = True)

ax = plt.gca()
merged.plot(kind = 'line', y = COAST_COLUMN, x = COUNTRY_COLUMN ,ax=ax)
merged.plot(kind = 'line', y = SATISFACTION_COLUMN, x = COUNTRY_COLUMN ,ax=ax)

plt.grid(b = True, color = 'aqua', alpha = 0.1, linestyle = 'dashdot')
plt.show();
```


![png](team13_capstone_project_files/team13_capstone_project_16_0.png)


## References

* [data for the cost of living](https://www.kaggle.com/andytran11996/cost-of-living/)
* [base data for countries of the world](https://www.kaggle.com/fernandol/countries-of-the-world)
* [data for life expectancy from the WHO](https://www.kaggle.com/kumarajarshi/life-expectancy-who)
* [roshansharma_europe-datasets](https://www.kaggle.com/roshansharma/europe-datasets)

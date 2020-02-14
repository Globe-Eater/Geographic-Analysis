#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:20:53 2020

@author: kellenbullock
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def upper(x):
    '''Will convert all text to uppercase.'''
    return x.upper()

def replace(x):
    '''Cuts off the last part of county in the Names column.'''
    answer = x.replace('COUNTY', '')
    return answer

def main():
        
    oklahoma = gpd.read_file('/Users/kellenbullock/Documents/Gradschool/Geographic Analysis/Exercise 1/Mappin/COUNTY_BOUNDARY.shp')
    data = pd.read_csv('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex1/County_Data.csv')

    data['Name'] = data['Name'].apply(upper)
    data['Name'] = data['Name'].apply(replace)
    data = data.rename(columns={'Name': 'COUNTY_NAM'})
    
    # Combining the datasets. 
    oklahoma = oklahoma.join(data, lsuffix='COUNTY_NAM', rsuffix='COUNTY_NAM')

    fig, ax = plt.subplots(1, 1)
    ax.axis('off')
    ax.set_title('Pct_Poverty by County', fontdict={"fontsize": 14, "fontweight" : 3})
    oklahoma.plot(column='Pct_Poverty', ax=ax, scheme='equalinterval', k=5, legend=True, legend_kwds={'loc': 'lower left'})
    
if __name__ == '__main__':
    main()
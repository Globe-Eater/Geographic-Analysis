#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:00:13 2020

@author: kellenbullock
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import sys
sys.path.append('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex1')
import Map

data = pd.read_csv('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex4/Data_Vars.csv')
oklahoma = gpd.read_file('/Users/kellenbullock/Documents/Gradschool/Geographic Analysis/Exercise 1/Mappin/COUNTY_BOUNDARY.shp')

data['Name'] = data['Name'].apply(Map.upper)
data['Name'] = data['Name'].apply(Map.replace)
data = data.rename(columns={'Name': 'COUNTY_NAM'})

oklahoma = oklahoma.join(data, lsuffix='COUNTY_NAM', rsuffix='COUNTY_NAM')
oklahoma.plot(column='LEV_1')

fig, ax = plt.subplots(1, 1)
ax.axis('off')
ax.set_title('Leverage Values', fontdict={"fontsize": 14, "fontweight" : 3})
oklahoma.plot(column='LEV_1', ax=ax, scheme='equalinterval', k=5, legend=True, legend_kwds={'loc': 'lower left'})
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:03:02 2020

@author: kellenbullock

Use Map.py methods to make a chorlopehtic map of LQs

INFO!!!!! Repub. Edmond. Region 3
"""

# my assigned variables are Repbu and Edmond LQ1 and LQ2 respectively
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

def upper(x):
    '''Will convert all text to uppercase.'''
    return x.upper()

def replace(x):
    '''Cuts off the last part of county in the Names column.'''
    answer = x.replace('COUNTY', '')
    return answer

votes = pd.read_excel('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/OSEB_18_Counties.xlsx')
canadiate = pd.read_excel('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/OSEB_18_Counties.xlsx', sheet_name="Governor 2018")

votes['LQ1'] = ''
votes['LQ1'] = ((votes['Total']/votes['Republican'])/(votes['Total'].sum()/votes['Republican'].sum()))


canadiate['LQ2'] = ''
canadiate['LQ2'] = ((canadiate['Total']/canadiate['Edmondson (D)'])/(canadiate['Total'].sum()/canadiate['Edmondson (D)'].sum()))

votes = votes[['County', 'Republican', 'Total', 'LQ1']]
canadiate = canadiate[['County', 'Edmondson (D)', 'Total', 'LQ2']]

votes = votes.rename(columns={'Total': 'Total Registered Voters'})
votes['Total Governor Votes'] = ''
votes['Total Governor Votes'] = canadiate['Total']
votes['Edmondson (D)'] = ''
votes['LQ2'] = ''
votes['LQ2'] = canadiate['LQ2']
votes['Edmondson (D)'] = canadiate['Edmondson (D)'] 
canadiate.to_excel('Edmondson.xlsx')
# Save out file
votes.to_excel('Bullock_2.xlsx')

# Mapping section:
oklahoma = gpd.read_file('/Users/kellenbullock/Documents/Gradschool/Geographic Analysis/Exercise 1/Mappin/COUNTY_BOUNDARY.shp')
data = pd.read_excel('/Users/kellenbullock/Desktop/Bullock_2.xlsx')

data['County'] = data['County'].apply(upper)
data['County'] = data['County'].apply(replace)
data = data.rename(columns={'County': 'COUNTY_NAM'})

oklahoma = oklahoma.join(data, lsuffix='COUNTY_NAM', rsuffix='COUNTY_NAM')

# LQ2
fig, ax = plt.subplots(1, 1)
ax.axis('off')
ax.set_title('Location quotients for Republican ', fontdict={"fontsize": 14, "fontweight" : 3})
oklahoma.plot(column='LQ1', ax=ax, scheme='naturalbreaks', k=4, legend=True, legend_kwds={'loc': 'lower left'})

# LQ2
fig2, ax2 = plt.subplots(1, 1)
ax2.axis('off')
ax2.set_title('Location quotients for Edmondson (D)', fontdict={"fontsize": 14, "fontweight" : 3})
oklahoma.plot(column='LQ2', ax=ax2, scheme='equalinterval', k=5, legend=True, legend_kwds={'loc': 'lower left'})
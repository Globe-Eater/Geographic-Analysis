#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:20:37 2020

@author: kellenbullock
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from Part_A import figures, Descrptives

path = '/users/kellenbullock/desktop/Geographic Analysis II/Data/'

milwaukee_raw = pd.read_spss(path + '5303_EX_B.sav')

milwaukee = milwaukee_raw.drop(columns=['Record', 'SaleDate', 'Ald', 'X', 'Y'])

def convert(string):
    '''Inputs a string yes or no and converts to 1 or 0'''
    if string == 'Yes':
        return 1
    elif string == 'No':
        return 0
    else:
        return "We've got a problem."

milwaukee['Basement'] = milwaukee['Basement'].apply(convert)
milwaukee['AC'] = milwaukee['AC'].apply(convert)
milwaukee['Attic'] = milwaukee['Attic'].apply(convert)
milwaukee['Garage'] = milwaukee['Garage'].apply(convert)

milwaukee = milwaukee.drop(columns=['Basement', 'AC', 'Attic', 'Garage'])

#figures(milwaukee, '')
#gdf = gpd.GeoDataFrame(milwaukee_raw, geometry=gpd.points_from_xy(milwaukee_raw.Y, milwaukee_raw.X))
#plt.show()
Descrptives(milwaukee, milwaukee)



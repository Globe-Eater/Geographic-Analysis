#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:45:57 2020

@author: Kellen Bullock
"""

import math
import pandas as pd
import sys
sys.path.append('/Users/kellenbullock/desktop/Geographic Analysis II/Ex1')
import EDA


def log_transformation(df):
    '''This method takes in a dataframe series and applys the log base 10
    transformation. 
    This method will print out a Shprio Wilks and Kolmogorov-Smirnov test 
    statstics.
    
    inputs:
        pandas series or array.
    
    returns:
        transformated pandas series or array
        2 print lines of normality tests
        
    Usage:
        log_transformation(df)
        
    '''
        

#def main():
state = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_A.sav')

Counties = state.query("Scale == 'Counties'")
Schools = state.query("Scale == 'Schools'")
Tracts = state.query("Scale == 'Tracts'")

# Old varaibles:
assigned_var_c = Counties[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]
assigned_var_s = Schools[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]
assigned_var_t = Tracts[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]

assigned_var_t = assigned_var_t.reset_index()
assigned_var_s = assigned_var_s.reset_index()
assigned_var_s = assigned_var_s.drop(columns=['index'])
assigned_var_t = assigned_var_t.drop(columns=['index'])

# New Variables 
var_c = Counties[['Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
var_s = Schools[['Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
var_t = Tracts[['Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]

var_t = var_t.reset_index()
var_s = var_s.reset_index()
var_t = var_t.drop(columns=['index'])
var_s = var_s.drop(columns=['index'])

EDA.figures(var_c, 'Counties')
EDA.figures(var_s, 'Schools')
EDA.figures(var_t, 'Tracts')

EDA.Descrptives(Counties, var_c)
print('====== School Districts =======')
EDA.Descrptives(Schools, var_s)
print('======== Tracts =========')
EDA.Descrptives(Tracts, var_t)


# if __name__ == '__main__':
#    main()

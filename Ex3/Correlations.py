#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:45:57 2020

@author: Kellen Bullock
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import sys
sys.path.append('/Users/kellenbullock/desktop/Geographic Analysis II/Ex1')
import EDA
from Transformations import test_trans

def bivar_regres(independent, dependent):
    '''This method is for doing bivartie regression. In other words it only regresses
    two variables. 
    
    inputs:
        indenpendent = the independent variable
        
        dependent = the dependent variable
    
    returns:
        A statsmodels regression table to the console and
        saves it out to a pdf file.'''
    
    mod = sm.OLS(independent, dependent)
    res = mod.fit()
    print(res.summary())

#def main():
state = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_A.sav')

Counties = state.query("Scale == 'Counties'")
Schools = state.query("Scale == 'Schools'")
Tracts = state.query("Scale == 'Tracts'")

# Old varaibles:
assigned_var_c = Counties[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
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

# 1.
#EDA.figures(var_c, 'Counties')
#EDA.figures(var_t, 'Tracts')
#EDA.figures(var_s, 'Schools')

print('=====County=======')
#EDA.Descrptives(Counties, var_c)
print('======== Tracts =========')
#EDA.Descrptives(Tracts, var_t)
print('====== School Districts =======')
#EDA.Descrptives(Schools, var_s)

# 1 part b:
test_trans(assigned_var_c, 'Pct_Black')
print('************')
test_trans(assigned_var_c, 'Pct_Hispanic')

# 3. 
assigned_c_repub = Counties[['Pct_Repub', 'Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
assigned_c_repub = assigned_c_repub.reset_index()
assigned_c_repub = assigned_c_repub.drop(columns=['index'])

# This will make a pearson's r correlation matrix at the County scale
# These do not work in the spyder IDE. Please see the jupyter notebook for outputs.
corr = assigned_var_c.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(3)

corr2 = assigned_c_repub.corr()
corr2.style.background_gradient(cmap='coolwarm').set_precision(3)

EDA.df_to_pdf(corr, 'Matrix_1')
EDA.df_to_pdf(corr2, 'Matrix_2')

''' Easy way to order Correlations but without signs:
    correlations = assigned_var_c.corr().abs()
    stack = correlations.unstack()
    stack_order = s.sort_values(kind='quicksort')
'''
# 2. a. 8 strongest Person's correaltions
corr_table = {
    'Variables': ['Pct_Poverty / Pct_SNAP', 'Pct_Unemp / Pct_SNAP', 'Pct_White / Pct_Unemp', 'Pct_White / Pct_SNAP', 'Pct_Unemp / Pct_Poverty', 'Pct_White / Pct_Two_Plus', 'Pct_White / Pct_Poverty', 'Pct_Fire_I / Pct_BlueCollar_O'],
    'Correlation': [0.757, 0.722, - 0.672, - 0.645, 0.605, - 0.599, - 0.593, - 0.574]
    }

pearson_r_table = pd.DataFrame(corr_table)
EDA.df_to_pdf(pearson_r_table, 'Decending_corr')

#EDA.merge_pdfs()


# if __name__ == '__main__':
#    main()

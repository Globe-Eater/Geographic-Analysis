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

def log_trans(df, column):
    '''This method takes in a dataframe series and applys the log base 10
    transformation. 
    This method will print out a Shprio Wilks and Kolmogorov-Smirnov test 
    statstics.
    
    inputs:
        df is the name of the DataFrame
        column is the name of the column within the DataFrame to be used.  
            column must be a string.
    
    returns:
        transformated pandas series or array
        2 print lines of normality tests
        
    Usage:
        log_transformation(Monsters['Rabbits'])
        
    '''
    df = np.log10(df[column])
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df
        
def sqrt_trans(df, column):
    ''' This method takes the input of a dataframe name and a column name.
    This will return a square root transformation of the input series.
    
    inputs:
        df = the name of the pandas Dataframe
        column = the name of the series or column.
        
    returns:
        A qq plot of result of the transformation.
        2 print statements of Shaprio Wilks and Kolmogorov-Smirnov tests.
        The newly transformed series.
        
    Usage:
        Monsters['Rabbit'] = sqrt_trans(Monsters, 'Rabbit')'''
    df = np.sqrt(df[column])
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df

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
assigned_c_repub = Counties[['Pct_Repub', 'Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
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
EDA.figures(var_t, 'Tracts')
EDA.figures(var_s, 'Schools')

print('=====County=======')
EDA.Descrptives(Counties, var_c)
print('======== Tracts =========')
EDA.Descrptives(Tracts, var_t)
print('====== School Districts =======')
EDA.Descrptives(Schools, var_s)

EDA.merge_pdfs()
#stats.pearsonr(x, y)

# This will make a pearson's r correlation matrix at the County scale
# These do not work in the spyder IDE. Please see the jupyter notebook for outputs.
corr = assigned_var_c.corr()
corr.style.background_gradient(cmap='coolwarm')

#EDA.merge_pdfs()


# if __name__ == '__main__':
#    main()

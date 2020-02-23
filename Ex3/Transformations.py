#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:35:42 2020

@author: kellenbullock
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

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

def expo_trans(df, column, factor):
    '''This method will transform the input data by a exponet specified by the user.
    
    inputs:
        df = dataframe name. Dataframe object
        column = the column to be transformed within the dataframe. String object
        factor = a number. Int
        
    returns:
        A qq plot of the result of the transformation.
        2 print statments of the Shaprio-Wilks and Kolmogorov-Smirnov tests.
        Newly transformed series.
        
    Usage:
        Oklahoma['Pct_SNAP'] = expo_trans(Oklahoma, 'Pct_SNAP', 2)'''
    df = df[column]**2
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df

def sin_trans(df, column):
    ''' This method takes the input of a dataframe name and a column name.
    This will return a sin transformation of the input series.
    
    inputs:
        df = the name of the pandas Dataframe
        column = the name of the series or column.
        
    returns:
        A qq plot of result of the transformation.
        2 print statements of Shaprio Wilks and Kolmogorov-Smirnov tests.
        The newly transformed series.
        
    Usage:
        Monsters['Rabbit'] = sqrt_trans(Monsters, 'Rabbit')'''
    df = np.sin(df[column])
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df

def cos_trans(df, column):
    ''' This method takes the input of a dataframe name and a column name.
    This will return a cos transformation of the input series.
    
    inputs:
        df = the name of the pandas Dataframe
        column = the name of the series or column.
        
    returns:
        A qq plot of result of the transformation.
        2 print statements of Shaprio Wilks and Kolmogorov-Smirnov tests.
        The newly transformed series.
        
    Usage:
        Monsters['Rabbit'] = sqrt_trans(Monsters, 'Rabbit')'''
    df = np.cos(df[column])
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df

def tan_trans(df, column):
    ''' This method takes the input of a dataframe name and a column name.
    This will return a tan transformation of the input series.
    
    inputs:
        df = the name of the pandas Dataframe
        column = the name of the series or column.
        
    returns:
        A qq plot of result of the transformation.
        2 print statements of Shaprio Wilks and Kolmogorov-Smirnov tests.
        The newly transformed series.
        
    Usage:
        Monsters['Rabbit'] = sqrt_trans(Monsters, 'Rabbit')'''
    df = np.tan(df[column])
    sm.qqplot(df, line='r')
    print('Shaprio Wilks test: ', stats.shapiro(df))
    print('Kolmogorov-Smirnov: ', stats.kstest(df, 'norm'))
    print("")
    return df

def test_trans(df, column):
    '''When called will ask user for input on what dataframe and column to transform.
    This will run a natural log, square root, expoential, sin, cos, and tan transformation.
    
    return: 
        qq-plots of the transformations and print lines for normality tests.
    '''
    log_trans(df, column)
    sqrt_trans(df, column)
    expo_trans(df, column, 2)
    sin_trans(df, column)
    cos_trans(df, column)
    tan_trans(df, column)
    print("Done.")
    

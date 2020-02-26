#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:45:57 2020

@author: Kellen Bullock
"""

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
sys.path.append('/Users/kellenbullock/desktop/Geographic Analysis II/Ex1')
import EDA
import Transformations
import Partial_Corr

def corr_scatter(df, x, y):
    '''This method will create a scatter plot of two variables using y as the static y axis.
    
    input: 
        df = dataframe
        x = the variable to sit upon the x axis. A list of strings.
        y = the static variable that will stay on the y axis. String
        
    output:
        scatter plots titled with repsected variables.
    
    Usage:
        corr_scatter(corr3, 'Pct_Poverty', 'Pct_Repub')
        '''
    for x in df:
        df.plot(kind='scatter', x=x, y=y).set_title(x + ' vs ' + y)
        plt.savefig(x + ' vs ' + y + '_scatter.pdf')
        
def bivar_regres(dependent, independent):
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
    res_sum = res.summary()

    fig = plt.figure()
    ax = fig.add_subplot()
    sm.qqplot(res.resid, line='r', ax=ax)    
    #fig.suptitle(dependent + ' vs ' + independent, fontsize=14)
    #plt.savefig(dependent + ' vs ' + independent + '_qqplot.pdf')

    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    residual = res.resid
    residual.plot(kind='hist', ax=ax2)
    #fig.suptitle(dependent + ' vs ' + independent, fontsize=14)
    #plt.savefig(dependent + ' vs ' + independent + '_qqplot.pdf')

        
    # Note that tables is a list. The table at index 1 is the "core" table. Additionally, read_html puts dfs in a list, so we want index 0
    results_as_html = res_sum.tables[1].as_html()
    df = pd.read_html(results_as_html, header=0, index_col=0)[0]
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values,colLabels=df.columns,loc='center')
    
    print(res.summary())
    EDA.df_to_pdf(df, path=independent.name + ' regression')
    print(independent.name + ' regression')
    

#def main():
state = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_A.sav')

Counties = state.query("Scale == 'Counties'")
Schools = state.query("Scale == 'Schools'")
Tracts = state.query("Scale == 'Tracts'")


assigned_var_c = Counties[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
assigned_var_s = Schools[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]
assigned_var_t = Tracts[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]

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
#test_trans(assigned_var_c, 'Pct_Black')
print('************')
#test_trans(assigned_var_c, 'Pct_Hispanic')

# 2,
# This will make a pearson's r correlation matrix at the County scale
# These do not work in the spyder IDE. Please see the jupyter notebook for outputs.
corr = assigned_var_c.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(3)

EDA.df_to_pdf(corr, 'Matrix_1')

''' Easy way to order Correlations but without signs:
    correlations = assigned_var_c.corr().abs()
    stack = correlations.unstack()
    stack_order = s.sort_values(kind='quicksort')
'''
# 2. a. 8 strongest Person's correaltions. There was no easy way to do this I had to pull everythong by hand.
corr_table = {
    'Variables': ['Pct_Poverty / Pct_SNAP', 'Pct_Unemp / Pct_SNAP', 'Pct_White / Pct_Unemp', 'Pct_White / Pct_SNAP', 'Pct_Unemp / Pct_Poverty', 'Pct_White / Pct_Two_Plus', 'Pct_White / Pct_Poverty', 'Pct_Fire_I / Pct_BlueCollar_O'],
    'Correlation': [0.757, 0.722, - 0.672, - 0.645, 0.605, - 0.599, - 0.593, - 0.574]
    }

all_scale = {
     'Variables': ['Pct_Poverty / Pct_SNAP', 'Pct_Unemp / Pct_SNAP', 'Pct_White / Pct_Unemp', 'Pct_White / Pct_SNAP', 'Pct_Unemp / Pct_Poverty', 'Pct_White / Pct_Two_Plus', 'Pct_White / Pct_Poverty', 'Pct_Fire_I / Pct_BlueCollar_O'],
    'County': [0.757, 0.722, - 0.672, - 0.645, 0.605, - 0.599, - 0.593, - 0.574],
    'Tract': [0.773, 0.679, -0.474, -0.564, 0.628, -0.296, -0.495, -0.584],
    'School District': [0.732, 0.590, -0.440, -0.515, 0.494, -0.569, -0.442, -0.380]
    }

pearson_r_table = pd.DataFrame(corr_table)
pearson_r_table.to_excel('County Correlation.xlsx')
EDA.df_to_pdf(pearson_r_table, 'Decending_corr')

all_scale = pd.DataFrame(all_scale)
all_scale.to_excel('Scale_Correlation.xlsx')
EDA.df_to_pdf(all_scale, 'Scale_Correlation')

# 3. 
assigned_c_repub = Counties[['Pct_Repub', 'Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Pct_Unemp', 'Med_HomeValue', 'Pct_White', 'Pct_BlueCollar_O', 'Pct_Hispanic']]

assigned_c_repub = assigned_c_repub.reset_index()
assigned_c_repub = assigned_c_repub.drop(columns=['index'])
assigned_c_repub['Pct_Black'] = Transformations.log_trans(assigned_c_repub, 'Pct_Black')
assigned_c_repub['Pct_Hispanic'] = Transformations.log_trans(assigned_c_repub, 'Pct_Hispanic')

corr2 = assigned_c_repub.corr()
corr2.style.background_gradient(cmap='coolwarm').set_precision(3)
EDA.df_to_pdf(corr2, 'Matrix_2')

# c.
chosen = corr2[['Pct_Repub', 'Pct_Poverty', 'Pct_Unemp', 'Pct_White', 'Pct_SNAP']]
x = ['Pct_Repub', 'Pct_Poverty', 'Pct_Unemp', 'Pct_White', 'Pct_SNAP']
y = 'Pct_Repub'
corr_scatter(chosen, x, y)

# c. 4 scatter plots with y axis being pct_republican

chosen = assigned_c_repub[['Pct_Repub', 'Pct_Poverty', 'Pct_Unemp', 'Pct_White', 'Pct_SNAP']]
corr3 = Partial_Corr.partial_corr(chosen)
corr3 = pd.DataFrame(corr3, index=['Pct_Repub', 'Pct_Poverty', 'Pct_Unemp', 'Pct_White', 'Pct_SNAP'], columns=['Pct_Repub', 'Pct_Poverty', 'Pct_Unemp', 'Pct_White', 'Pct_SNAP'])

EDA.df_to_pdf(corr3, 'Matrix3')

# 5.
bivar_regres(chosen['Pct_Repub'], chosen['Pct_Poverty']) # Model 1
bivar_regres(chosen['Pct_Repub'], chosen['Pct_SNAP'])    # Model 2
bivar_regres(chosen['Pct_Repub'], chosen['Pct_White'])   # Model 3
bivar_regres(chosen['Pct_Repub'], chosen['Pct_Unemp'])   # Model 4

#EDA.merge_pdfs()

# if __name__ == '__main__':
#    main()

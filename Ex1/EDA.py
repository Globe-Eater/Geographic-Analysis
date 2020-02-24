#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:34:09 2020
@author: kellenbullock
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from PyPDF2 import PdfFileMerger
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

def merge_pdfs():
    '''When called will gather all .pdfs and combine them as one file.
    Users should change the file name.'''
    filename = input("Please input fileanme, ex Lastname_Exercise#: ")
    x = [a for a in os.listdir() if a.endswith(".pdf")]
    print(x)
    merger = PdfFileMerger()
    for pdf in x:
        merger.append(open(pdf, 'rb'))
    with open(filename + ".pdf", "wb") as fout:
        merger.write(fout)
    print('Done.')
    
def df_to_pdf(df, path):
    '''This method will saveout a dataframe to a pdf file.
    
    inputs;
        df = pandas dataframe
        pathname = path/to/destination
    returns:
        a named pdf
    
    Usage:
        df_to_pdf(Oklahoma, "/Users/you/Geographic Analysis/Correlation")
    '''
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
    pp = PdfPages(filename=path + "_table.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

def figures(assigned_var, scale):
    '''This method takes a dataframe as input and outputs all the required
    histograms, boxplots, scatter plots, and qq-plots for Exericse 1
    Inputs:
        assigned_var = input variables a list of pandas series
        scale = County, Tracts, or School District. Must be a String.
        path = destination/for/save/location
        
    Returns:
        All graphs to plot panel in Spyder.
        Saves all graphs to pdfs. 
        
    Usage figures(var_t, 'Tracts', Ex3/Graphs/)
    '''
    # Histograms
    plt.clf()
    for columns in assigned_var:
        ax1 = sns.distplot(assigned_var[columns]).set(ylabel="Frequency", title=columns + " " + scale)
        plt.savefig(columns +  '' + scale + '_hist.pdf')
        plt.show()
    # Boxplots
    for columns in assigned_var:
        ax2 = sns.boxplot(data=assigned_var[columns]).set_title(columns + " " + scale)
        #ax2 = sns.swarmplot(data=assigned_var[columns], color="Black").set_title(columns)
        plt.savefig(columns + '' + scale + '_boxplot.pdf')
        plt.show()
    # Scatterplots
    for columns in assigned_var:
        ax3 = sns.scatterplot(data=assigned_var[columns]).set_title(columns + " " + scale)
        plt.savefig(columns + '' + scale + '_scatterplot.pdf')
        plt.show()
    # QQ plots
    for columns in assigned_var:
        fig = sm.qqplot(assigned_var[columns], line='r')
        fig.suptitle(columns + " " + scale, fontsize=14)
        plt.savefig(columns + '' + scale + '_qqplot.pdf')
        fig.show()
    print('Done')
    
       
def Descrptives(scale, assigned_var):
    '''This method will provide measures of central tendency and distribution with
    the input of a dataframe.'''
    # Descrptives: I need varience, coeffection of varience, skewness and kurtosis
    table_list = []
    for columns in assigned_var:
        table = {
            columns : '',
            'Skewness: ': scale[columns].skew(),
            'Kurtosis: ': scale[columns].kurtosis(),
            'Variance: ': scale[columns].var(),
            'Shaprio Wilks: ': stats.shapiro(scale[columns]),
            'Kolmogorov-Smirnov test: ': stats.kstest(scale[columns], 'norm'),
            'Mean: ': scale[columns].mean(),
            'Standard Deviation: ': scale[columns].std(),
            
        }
        print(columns)
        print('Skewness: ', scale[columns].skew())
        print('Kurtosis: ', scale[columns].kurtosis())
        print('Variance: ', scale[columns].var(),)
        print('Shaprio Wilks: ', stats.shapiro(scale[columns]))
        print('Kolmogorov-Smirnov test: ', stats.kstest(scale[columns], 'norm'))
        print('Descprtives', scale[columns].describe())
        print('')
        table_list.append(table)
    for tables in table_list:
        df = pd.DataFrame(tables)
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
        key = list(tables.keys())[0]
        pp = PdfPages(filename=key + "_table.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()
        
def main():
    path = '/users/kellenbullock/desktop/Geographic Analysis II/Data/'
    
    state = pd.read_spss(path + '5303_EX_A.sav')
    
    Counties = state.query("Scale == 'Counties'")
    Schools = state.query("Scale == 'Schools'")
    Tracts = state.query("Scale == 'Tracts'")
    
    # .info .describe for all of them will help the EDA
    
    # These are my variables:
    assigned_var_c = Counties[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]
    assigned_var_s = Schools[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]
    assigned_var_t = Tracts[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']]
    assigned_var_t = assigned_var_t.reset_index()
    assigned_var_s = assigned_var_s.reset_index()
    assigned_var_s = assigned_var_s.drop(columns=['index'])
    assigned_var_t = assigned_var_t.drop(columns=['index'])
    
    columns = ['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty']        
    
    figures(assigned_var_c, 'Counties')
    figures(assigned_var_t, 'Tracts')
    figures(assigned_var_s, 'School Districts')
    
    Descrptives(Counties, assigned_var_c)
    print("                   ")
    print('__________Tracts__________')
    Descrptives(Tracts, assigned_var_t)
    print("                   ")
    print('__________Schools__________')
    Descrptives(Schools, assigned_var_s)       
    merge_pdfs()
    
    
    select = state[['Pct_Black', 'Pct_Two_Plus', 'Pct_SNAP', 'Pct_FIRE_I', 'Pct_Poverty', 'Scale', 'Region']]
    plt.clf()
    # 1 Variable all three scales boxplots
    for columns in select:
        sns.boxplot(x="Scale", y=columns, data=select).set_title(columns)
        plt.show()
        
    plt.clf()
    no_na = select[0:76]
    # 1 Variable all Regions boxplots
    for columns in no_na:
        ax = sns.boxplot(x="Region", y=columns, data=no_na).set_title(columns + " by Region")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    main()
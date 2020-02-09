#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:16:57 2020

@author: kellenbullock
"""

# Milwaukee 2012 my months are: 08, 09, and 10
import pandas as pd
from Part_A import unweighted_centroid, weighted_Centroid, std_dist

# read data in:
Milwaukee = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_B.sav')

# Select month 08
august = Milwaukee[Milwaukee['SaleDate'] == '2012-08']
# Select month 09
sept = Milwaukee[Milwaukee['SaleDate'] == '2012-09']
# Select month 10
october = Milwaukee[Milwaukee['SaleDate'] == '2012-10']

# run unweighted_cent on all
august_cent_x, august_cent_y = unweighted_centroid(august['X'], august['Y'], 140)
sept_cent_x, sept_cent_y = unweighted_centroid(sept['X'], sept['Y'], 136)
october_cent_x, october_cent_y = unweighted_centroid(october['X'], october['Y'], 134)

# run std_dis for all 
august_std_dist = std_dist(august['X'], august['Y'], 140)
sept_std_dist = std_dist(sept['X'], sept['Y'], 136)
october_std_dist = std_dist(october['X'], october['Y'], 134)

# Saleprice.mean() for each month
august_Sale_Mean = august['SalePrice'].mean()
sept_Sale_Mean = sept['SalePrice'].mean()
october_Sale_Mean = october['SalePrice'].mean()

# Saleprice.std() for each month
august_Sale_std = august['SalePrice'].std()
sept_Sale_std = sept['SalePrice'].std()
october_Sale_std = october['SalePrice'].std()

# put all data into a table will probs be dictionary into pandas df
dataset = {
    "Month" : ["August", "September", "October"],
    "Centroids": [[august_cent_x, august_cent_y], [sept_cent_x, sept_cent_y], [october_cent_x, october_cent_y]],
    "Standard Distances" : [august_std_dist, sept_std_dist, october_std_dist],
    "Sale Mean" : [august_Sale_Mean, sept_Sale_Mean, october_Sale_Mean],
    "Sale Standard Distances" : [august_Sale_std, sept_Sale_std, october_Sale_std]
    }

final = pd.DataFrame(dataset)
# map it all!
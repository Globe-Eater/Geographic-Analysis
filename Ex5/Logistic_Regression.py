#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:58:21 2020

@author: kellenbullock
"""

import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_A.sav')
county = df[df.Scale == 'Counties']

dep = county[['Pct_Poverty']]
indep = county[['Density','Pct_Black','Pct_NatAm','Pct_Asian','Pct_Pacific','Pct_Other',
                      'Pct_Two_Plus','Pct_Hispanic','Med_Age','Pct_NotLabor','Pct_Unemp',
                      'Pct_Commute','Pct_Service_O','Pct_BlueCollar_O','Pct_FIRE_I','Pct_SNAP',
                      'PCI','Pct_Vacant','Med_HomeValue','Pct_Divorced','Pct_NoHS',
                      'Pct_Repub']]

# kitchen sink
model = sm.OLS(dep, indep)
results = model.fit()
results = results.summary()
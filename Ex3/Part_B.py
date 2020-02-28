#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:20 2020

@author: kellenbullock
"""

import pandas as pd
from pandas.plotting import scatter_matrix
import Correlations

Milkwaukee = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_B.sav')

Milkwaukee = Milkwaukee.drop(columns=['SaleDate', 'AC', 'Garage', 'Attic', 'Ald', 'Basement', 'Record'])

df = Milkwaukee.corr()

df = Correlations.unstack_corr(df)

# t-test:


# Correaltions by month
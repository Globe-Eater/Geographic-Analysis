#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:03:02 2020

@author: kellenbullock

Use Map.py methods to make a chorlopehtic map of LQs

INFO!!!!! Repub. Edmond. Region 3
"""

# my assigned variables are Repbu and Edmond LQ1 and LQ2 respectively

import pandas as pd

votes = pd.read_excel('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/OSEB_18_Counties.xlsx')
canadiate = pd.read_excel('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/OSEB_18_Counties.xlsx', sheet_name="Governor 2018")

votes['LQ1'] = ''
votes['LQ1'] = ((votes['Total']/votes['Republican'])/(votes['Total'].sum()/votes['Republican'].sum()))


canadiate['LQ2'] = ''
canadiate['LQ2'] = ((canadiate['Total']/canadiate['Edmondson (D)'])/(canadiate['Total'].sum()/canadiate['Edmondson (D)'].sum()))


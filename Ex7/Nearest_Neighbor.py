#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:20:12 2020

@author: kellenbullock
Data was geneerated from SPSS copied and pasted into excel and then read into
pandas. The Goal is to select the smallest values for each record.
"""
import pandas as pd

df = pd.read_excel('/Users/kellenbullock/Downloads/Distance Matrix.xlsx')

df.columns = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
              24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,
              44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,
              64,65,66,67,68,69,70,71,72,73]

df = df.replace(0.0, value=99999)
nn = []
for label, content in df.items():
    print(content.min())
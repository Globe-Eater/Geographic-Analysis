#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:44:55 2020
@author: Globe-Eater

Big thanks to the team at Pysal, here is the reference to this library:
https://pysal.org/notebooks/explore/pointpats/Quadrat_statistics.html
"""
import geopandas as gpd
import numpy as np
from pointpats import PointPattern, as_window
import pointpats.quadrat_statistics as qs

df = gpd.read_file('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex7/Data.shp')

points = df[['longitude','latitude']]
points = np.array(points)

pp_quakes = PointPattern(points)
pp_quakes.summary()

pp_quakes.plot(window= True, title= "Point pattern")

q_r = qs.QStatistic(pp_quakes,shape= "rectangle",nx = 4, ny = 4)
q_r.plot()

print("\n", q_r.chi2) #chi-squared test statistic for the observed point pattern
print("\n", q_r.df)
print("\n", q_r.chi2_pvalue) # analytical pvalue
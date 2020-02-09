#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:47:08 2020

@author: kellenbullock
"""

import pandas as pd
import numpy as np
from math import sqrt
from pysal.explore.pointpats import PointPattern
from pysal.explore.pointpats.centrography import euclidean_median


def unweighted_centroid(lat, long, number_obs):
    '''This method requires the input of 2 list of lat and long.
    The third input is the number of observations
    It will return 2 items the first item is lat and
    the second is long.
    Ex using pandas dataframes:
        unweighted_centroid(tracts['Lat_Cent'], tracts['Lon_Cent'], 1048)'''
    unweighted_Lat = lat.sum() / number_obs
    unweighted_Long = long.sum() / number_obs
    return unweighted_Lat, unweighted_Long

def weighted_Centroid(lat, long, weights):
    '''This method requires the inputs of list of Latiitude, Longitiude, and Weights.
    It will return 2 variables be sure to specify weighted_lat = weighted_long = weighted_Centroid()'''
    weighted_Lat = (lat * weights).sum() / weights.sum()
    weighted_Long = (long * weights).sum() / weights.sum()
    return weighted_Lat, weighted_Long


def std_dist(Lat, Long, number_samples):
    '''This method calculates standard distance.
    Requires dataframe inputs ie tracts['Lat_Cent']
    Inputs:
        x = the x coordinate aka Latitiude
        y = the y coordinate aka Longitude
        number_samples = n
        weights = optional put None is nothing is needed.
    Returns standard distiance'''
    Lat_mean = Lat.mean()
    Long_mean = Long.mean()
    std_unweighted = sqrt( (np.sum((Lat - Lat_mean)**2) + np.sum((Long - Long_mean)**2)) / number_samples  )
    return std_unweighted

def weighted_std_dist(Lat, Long, weights):
    '''This method requires list inputs of lat, long and weights.
    It will return 1 int of the weighted Standard Distance.'''
    #std_weighted = sqrt((weights.sum() * Lat.var() + weights.sum() * Long.var()) / weights.sum())
    Lat_mean = Lat.mean()
    Long_mean = Long.mean()
    std_weighted = sqrt( ((np.sum(weights * (Lat - Lat_mean)**2)) + np.sum(weights * (Long - Long_mean)**2)) / np.sum(weights))
    return std_weighted

''' WAAAYYY to tried to work on this right now. Using pysal library instead.
def Median_Center(Lat, Long, weights, start_Lat, start_Long):
    Inputs requried are arrays of Latitiude, Longitide
    and weights. Will iterate 5 times.
    Outputs: are 2 variables x and y coordinates.
    Usage:
        median_Lat, median_Long = Median_Center()
    
    np.sum(weights * Lat) / np.sum(start_Lat)
    
    return #2 things
'''

def main():
    
    oklahoma = pd.read_spss('/Users/kellenbullock/Desktop/Geographic Analysis II/Data/5303_EX_A.sav')
    
    # offical Census centroid for Oklahoma: as of 2010
    Census_lat = 35.572285
    Census_Long = -97.043688
    
    # Selecting features only at the tract scale.
    tracts = oklahoma[oklahoma.Scale == "Tracts"]
    # number of obs in Tracts
    n = 1046
    
    unweighted_Lat, unweighted_Long = unweighted_centroid(tracts['Lat_Cent'], tracts['Lon_Cent'], n)
    pop_weighted_Lat, pop_weighted_Long = weighted_Centroid(tracts['Lat_Cent'], tracts['Lon_Cent'], tracts['Population'])
    area_weighted_Lat, area_weighted_Long = weighted_Centroid(tracts['Lat_Cent'], tracts['Lon_Cent'], tracts['Area'])
    
    
    unweighted_std_dist = std_dist(tracts['Lat_Cent'], tracts['Lon_Cent'], n)
    pop_weighted_std_dist = weighted_std_dist(tracts['Lat_Cent'], tracts['Lon_Cent'], tracts['Population'])
    area_weighted_std_dist = weighted_std_dist(tracts['Lat_Cent'], tracts['Lon_Cent'], tracts['Area'])
    
    region3 = oklahoma[oklahoma.Region == 'South Central']
    region3_Lat_unweighted_cent, region3_Long_unweighted_cent = unweighted_centroid(region3['Lat_Cent'], region3['Lat_Cent'], 15)
    region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long = weighted_Centroid(region3['Lat_Cent'], region3['Lon_Cent'], region3['Population'])
    
    # pysal to the rescue!
    points = zip(region3['Lat_Cent'], region3['Lon_Cent'])
    pp = PointPattern(points)
    em = euclidean_median(pp.points)
    
    # DataFrame for all data:
    dataset_state = {
        "Unweighted Centroid": [[unweighted_Lat, unweighted_Long]],
        "Population Weighted Centroid": [[pop_weighted_Lat, pop_weighted_Long]],
        "Area Weighted Centroid": [[area_weighted_Lat, area_weighted_Long]],
        "Unweighted STD": [unweighted_std_dist],
        "Population Weighted STD": [pop_weighted_std_dist],
        "Area Weighted STD": [area_weighted_std_dist]
        }
    
    dataset_region = {
        "Region 3 Unweighted Centroid": [[region3_Lat_unweighted_cent, region3_Long_unweighted_cent]],
        "Region 3 Population Weighted Centroid": [[region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long ]]
        }
    
    

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:47:08 2020

@author: kellenbullock

Whats left:
    mean center equation, and weighted version....
    
    mapping all centroids and standard distances....
    
    writing out all answers....
"""

import pandas as pd
import geopandas as gpd
import numpy as np
from math import sqrt
from pysal.explore.pointpats import PointPattern
from scipy.optimize import minimize
from pysal.explore.pointpats.centrography import euclidean_median
import matplotlib.pyplot as plt
from shapely.geometry import Point
import fiona; fiona.supported_drivers

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

def dtot(coord, points):
    """
    Sum of Euclidean distances between event points and a selected point.

    Parameters
    ----------
    coord   : arraylike
              (x,y) coordinates of a point.
    points  : arraylike
              (n,2), (x,y) coordinates of a series of event points.

    Returns
    -------
    d       : float
              sum of Euclidean distances.

    """
    points = np.asarray(points)
    xd = points[:, 0] - coord[0]
    yd = points[:, 1] - coord[1]
    d = np.sqrt(xd*xd + yd*yd).sum()
    return d

def euclidean_median(points, region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long):
    """
    Calculate the Euclidean median for a point pattern.

    Parameters
    ----------
    points: arraylike
            (n,2), (x,y) coordinates of a series of event points.

    Returns
    -------
    _     : array
            (2,), (x,y) coordinates of the Euclidean median.

    """
    points = np.asarray(points)
    start = region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long
    res = []
    res.append(minimize(dtot, start, args=(points,), options={'maxiter':1}))
    res.append(minimize(dtot, start, args=(points,), options={'maxiter':2}))
    res.append(minimize(dtot, start, args=(points,), options={'maxiter':3}))
    res.append(minimize(dtot, start, args=(points,), options={'maxiter':4}))
    res.append(minimize(dtot, start, args=(points,), options={'maxiter':5}))
    return res


def upper(x):
    '''Will convert all text to uppercase.'''
    return x.upper()

def replace(x):
    '''Cuts off the last part of county in the Names column.'''
    answer = x.replace('COUNTY', '')
    return answer

#def main():
    
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
region_3_em = euclidean_median(pp.points, region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long)

# Shamefully I printed out all of these to the interperater and copy pasted them....
em_x = [region3_cent_weighted_pop_Lat, 34.75945234, 34.76199467, 34.762186, 34.76219894, 34.76219991]
em_y = [region3_cent_weighted_pop_Long, -97.55846305, -97.54911636, -97.54889305, -97.54889855, -97.54889943]

iterations = {
    'Iterations': ['Start', 1, 2, 3, 4, 5],
    'Euclidean Median Lat': em_x,
    'Euclidean Median Long': em_y
    }

# DataFrame for all data:
names = ["Unweighted Centroid", "Population Weighted Centroid", "Area Weighted Centroid", "Census Centroid"]
Latitude = [unweighted_Lat, pop_weighted_Lat, area_weighted_Lat, Census_lat]
Longitiude = [unweighted_Long, pop_weighted_Long, area_weighted_Long, Census_Long]

state_data = pd.DataFrame(data={'names': names,
                                'Latitude': Latitude,
                                'Longitiude': Longitiude})

dataset_state = {
    "Unweighted Centroid": [[unweighted_Lat, unweighted_Long]],
    "Population Weighted Centroid": [[pop_weighted_Lat, pop_weighted_Long]],
    "Area Weighted Centroid": [[area_weighted_Lat, area_weighted_Long]],
    "Unweighted STD": unweighted_std_dist,
    "Population Weighted STD": pop_weighted_std_dist,
    "Area Weighted STD": area_weighted_std_dist
    }

names = ["Region 3 Unweighted Centroid", 'Region 3 Population Weighted Centroid']
lat = [region3_Lat_unweighted_cent, region3_cent_weighted_pop_Lat]
long = [region3_Long_unweighted_cent,region3_cent_weighted_pop_Long]

Region_data = pd.DataFrame(data={'Names': names,
                                 'Latitude' : lat,
                                 'Longitutde': long})

dataset_region = {
    "Region 3 Unweighted Centroid": [[region3_Lat_unweighted_cent, region3_Long_unweighted_cent]],
    "Region 3 Population Weighted Centroid": [[region3_cent_weighted_pop_Lat, region3_cent_weighted_pop_Long ]]
    }

state_data.to_csv('Centoids.csv')
Pop_Area_Table = pd.DataFrame(dataset_state)
Region_Table = pd.DataFrame(dataset_region)
EU_Distance = pd.DataFrame(iterations)
EU_Distance.to_csv('EU_Median.csv')
Pop_Area_Table.to_excel('Table_1.xlsx')
Region_Table.to_excel('Table_2.xlsx')
Region_data.to_excel('Table_3.xlsx')

# Mappin: I could not finish this part with the time constrains of this exercise 2 weeks... Here is the start of mapping with GEOPANDAS
'''
State_Tracts = gpd.read_file('/Users/kellenbullock/Desktop/Geographic Analysis II/Ex2/tl_2018_40_tract/tl_2018_40_tract.shp') # Tracts shapefile
fig, ax = plt.subplots()

State_Tracts.plot(ax=ax, color='white', edgecolor='grey')
point_one = state_data[state_data.names == "Unweighted Centroid"]
point_one.plot(ax=ax, color='red', marker='o', label='Unweighted Centroid')


Region = gpd.read_file('/Users/kellenbullock/Documents/Gradschool/Geographic Analysis/Exercise 1/Mappin/COUNTY_BOUNDARY.shp') # County Shapefile
# Join Region 3 to Oklahoma County map
data = region3
data['Name'] = data['Name'].apply(upper)
data['Name'] = data['Name'].apply(replace)
data = data.rename(columns={'Name': 'COUNTY_NAM'})
    
# Combining the datasets. 
Region = Region.join(data, lsuffix='COUNTY_NAM', rsuffix='COUNTY_NAM')

# Select only Region 3
Region = Region[Region.Region == 'South Central']
# save this shapefile out and then map it in QGIS
Region = Region.drop(columns=['CREATION_D', 'LOGIN', 'PHONE_NO_B', 'DESC_LOCAT'])
Region.to_file(filename="Region_Map_Data.shp", driver="ESRI Shapefile")


fig1, ax1 = plt.subplots()

Region.plot(ax=ax1, color='white', edgecolor='black')
'''

#if __name__ == '__main__':
    #main()
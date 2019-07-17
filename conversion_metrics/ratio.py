'''Calculate conversion rates and related metrics.'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def conversion_rate(dataframe, column_names):
    '''Calculate conversion rate.

    Parmaters
    ---------
    dataframe: pandas.DataFrame
    column_names: str
             The conlumn(s) chosen to calculate
             conversion rate.

    Returns
    -------
    conversion_rate: conversion rate'''
    # Total number of converted users
    column_conv = dataframe[dataframe['converted'] == True] \
        .groupby(column_names)['user_id'] \
        .nunique()

    # Total number users
    column_total = dataframe \
        .groupby(column_names)['user_id'] \
        .nunique() 
    
    # Conversion rate 
    conversion_rate = column_conv/column_total
    
    # Fill missing values with 0
    conversion_rate = conversion_rate.fillna(0)
    return conversion_rate

def lift(a,b):
    '''Calculate lift statistic for an AB test.

    Parmaters
    ---------
    a: float.
        control group.
    b: float.
        test group.

    Returns
    -------
    lift: left statistic'''
    # Calcuate the mean of a and b
    a_mean = np.mean(a)
    b_mean = np.mean(b)

    # Calculate the lift using a_mean and b_mean
    lift = b_mean/a_mean - 1

    return str(round(lift*100, 2)) + '%'

def ab_segmentation(segment):
    '''Calculate lift statistic by segmentation.
    Only for marketing dataset.'''
  # Build a for loop for each segment in marketing
  for subsegment in np.unique(marketing.language_displayed.values):
      print(subsegment)
      
      # Limit marketing to email and subsegment      
      email = marketing[(marketing['marketing_channel'] == 'Email') & (marketing[segment] == subsegment)]

      subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
      subscribers = pd.DataFrame(subscribers.unstack(level=1)) 
      control = subscribers['control'].dropna()
      personalization = subscribers['personalization'].dropna()

      print('lift:', lift(control, personalization))
      print('t-statistic:', stats.ttest_ind(control, personalization), '\n\n')



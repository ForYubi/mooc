# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:01:24 2016

@author: Administrator
"""

import pandas as pd

#%%
#pd.Series?

#%%
animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))

#%%
numbers = [1, 2, 3]
print(pd.Series(numbers))

#%%
animals = ['Tiger', 'Bear', None]
print(pd.Series(animals))

#%%
numbers = [1, 2, None]
print(pd.Series(numbers))

#%%
import numpy as np
print(np.nan == None)
print(np.nan == np.nan)

#%%
print(np.isnan(np.nan))
#print(np.isnan(animals[-1]))  TypeError

#%%
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwonodo': 'South Korea'}
s = pd.Series(sports)
print(s)
print(s.index)
print(s['Golf'])
#print(s['Scotland']) TypeError

#%%
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
print(s['India'])
#print(s['Tiger']) TypeError

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
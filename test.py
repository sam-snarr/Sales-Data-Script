#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join
import pandas as pd

# mypath = os.path.dirname(os.path.abspath(__file__))

# directory where the python script is
dirpath = os.path.dirname(os.path.realpath(__file__))
print(listdir(dirpath))

# gets full path of all files in same directory as script if it contains keywords 'apptopia' or 'mighty'
onlyfiles = [join(dirpath, f) for f in listdir(dirpath) if isfile(join(dirpath, f)) and ('mighty' in f.lower() or 'apptopia' in f.lower())] #and f != os.path.basename(__file__)

# removes python script from onlyfiles using set subtraction
onlyfiles = set(onlyfiles) - set([os.path.abspath(__file__)])

# initialize arrays for dataframes
apptopia_df_array = []
mighty_df_array = []

print('onlyfiles: ', onlyfiles)
print('os.path.abspath(__file__):', os.path.abspath(__file__))

# adds each file to relevant array and gives it column with what platform it came from
for file in onlyfiles:
    #print(file)
    f = file.lower()
    temp_df = pd.read_csv(file)
    
    if ('apptopia' in f) and ('ios' in f):
        temp_df['Platform'] = 'iOS'
        apptopia_df_array.append(temp_df)
        
    elif ('apptopia' in f) and ('android' in f):
        temp_df['Platform'] = 'Android'
        apptopia_df_array.append(temp_df)
        
    elif ('mighty' in f) and ('ios' in f):
        temp_df['Platform'] = 'iOS'
        mighty_df_array.append(temp_df)
        
    elif ('mighty' in f) and ('android' in f):
        temp_df['Platform'] = 'Android'
        mighty_df_array.append(temp_df)
    else:
    	print('___At least one relevant file was not used___')
        

# concatenate dataframe arryas
apptopia_df = pd.concat(apptopia_df_array) 
mighty_df = pd.concat(mighty_df_array)

# merge dataframes on app name and platform
final_df = pd.merge(left=apptopia_df, right=mighty_df, left_on=['App Name', 'Platform'], right_on=['App_Name', 'Platform']) # may need to update left_on/right_on

# output csv
final_df.to_csv(r'final df.csv')

# close terminal
input('Enter to close')

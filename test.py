#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join
import pandas as pd

# mypath = os.path.dirname(os.path.abspath(__file__))

# directory where the python script is
dirpath = os.path.dirname(os.path.realpath(__file__))
print(listdir(dirpath))

onlyfiles = [join(dirpath, f) for f in listdir(dirpath) if isfile(join(dirpath, f)) and ('mighty' in f.lower() or 'apptopia' in f.lower())] #and f != os.path.basename(__file__)

onlyfiles = set(onlyfiles) - set([os.path.abspath(__file__)])

apptopia_df_array = []
mighty_df_array = []

print('onlyfiles: ', onlyfiles)
print('os.path.abspath(__file__):', os.path.abspath(__file__))

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
        

apptopia_df = pd.concat(apptopia_df_array) 
mighty_df = pd.concat(mighty_df_array)

final_df = pd.merge(left=apptopia_df, right=mighty_df, left_on=['App Name', 'Platform'], right_on=['App_Name', 'Platform'])

final_df.to_csv(r'final df.csv')
input('Enter to close')

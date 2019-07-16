# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:19:07 2019

@author: annaarkx
"""
import pandas as pd

data = pd.read_csv('/Users/path/to/thefile.csv')

def cleaning(data):
    data = pd.read_csv('/Users/path/to/thefile.csv')
    data['column_to_remove'] = data['needed_column']
    data = data.drop(
                  ['aa'],['bbb'] [...],
                   axis=1)
    data.to_csv('/Users/path/to/thefile.csv')
    return

# Remove all the rows w str 'N'
def remove_n(data):
    data = data.loc[data['needed_column'] != 'N']

    data.to_csv('/Users/path/to/thefile.csv')
    return

if __name__ == '__main__':
    cleaning(data)
    remove_n(data)

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:19:07 2019

@author: annaarkx
"""
import pandas as pd


data = pd.read_csv('/path/to/file/.csv')

def cleaning(data):
    data['Col1'] = data['Col2']
    data = data.drop(
                  ['Columnes', 'Columnes'],
                   axis=1)
    data.to_csv('/path/to/file/.csv')
    return

# Remove all the rows w str 'N'
def rem_n(data):
    col = data["Col1"].str.contains("N")
    for c in col.index:
        if col[c]==True:
            data = data.drop(axis=0, labels=c)
            data.to_csv('/path/to/file/.csv')
            return



if __name__ == '__main__':
    cleaning(data)
    rem_n(data)
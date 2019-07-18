# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:19:07 2019

@author: annaarkx
"""
import pandas as pd
import sys 

data = pd.read_csv('/Users/path/to/thefile.csv')

def cleaning(data):
    data = pd.read_csv('/Users/path/to/thefile.csv')
    data['column_to_remove'] = data['needed_column']
    data = data.drop(
                  ['aa'],['bbb'] [...],
                   axis=1)
  
    # Remove all the rows w str 'N'
    data = data.loc[data['needed_column'] != 'N']

    data.to_csv('/Users/path/to/thefile.csv')
    return

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--clean] file [file ...]')
        sys.exit(1)

    if args[0] == '--clean':
        cleaning(data)
        


if __name__ == '__main__':
    main()


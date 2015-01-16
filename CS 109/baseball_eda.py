# special IPython command to prepare the notebook for matplotlib
%matplotlib inline 
 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import StringIO
import zipfile
import csv

s = '/Users/Jeremy/python/lahman-csv.zip'
d = zipfile.ZipFile(s)
sal = d.extract('Salaries.csv')
tm = d.extract('Teams.csv')
    

salaries = pd.read_csv('Salaries.csv')
teams = pd.read_csv('Teams.csv')

print salaries.head()
print teams.head()

v = ['teamID', 'yearID']
groupbyyear = salaries.groupby(v, as_index = False)
summary = groupbyyear['salary'].sum()
print summary.head()

# Merge Dataframes
merge = pd.merge(teams, summary)

# reset index
merge.reset_index(inplace=True)

# Select relevant columns (function iloc from stack overflow)
merged = merge.iloc[:, (1,3,9,49)]
print merged.head()

merged_loop = merged
for x in range(1995,2005):
    merged_loop = merged[(merged.yearID == (x))]
    plt.scatter(merged_loop['W'], merged_loop['salary'])
    plt.xlabel('W')
    plt.ylabel('salary')
    plt.show()


import requests 
import StringIO
import numpy as np
import pandas as pd # pandas
import matplotlib.pyplot as plt # module for plotting 
import datetime as dt # module for manipulating dates and times
import numpy.linalg as lin # module for performing linear algebra operations
import scipy

url = "https://raw.githubusercontent.com/cs109/2014_data/master/exprs_GSE5859.csv"
exprs = pd.read_csv(url, sep=',')
print exprs.head()
exprs.index=exprs[exprs.columns[0]]
print exprs.head()

url = "https://raw.githubusercontent.com/cs109/2014_data/master/sampleinfo_GSE5859.csv"
sampleinfo = pd.read_csv(url)

exprs2 = exprs.ix[:, 1:]
itemOrder = sampleinfo['filename']
exprs2 = exprs2[itemOrder]
print exprs2.head()
print sampleinfo.head()
(exprs2.columns == sampleinfo.filename).all()

date = pd.to_datetime(sampleinfo.date)
date.head()

sampleinfo['elapsedInDays'] = pd.to_datetime(sampleinfo.date) - dt.date(2002, 10, 31)
print sampleinfo.head()
sampleinfo['elapsedInDays']

sampleinfoCEU = sampleinfo[sampleinfo['ethnicity'] == 'CEU']
sampleinfoCEU.head()

exprsCEU = exprs2

# set dataframe to cases we do not want to be included in final dataframe
a = sampleinfo[sampleinfo.ethnicity != 'CEU']
for i in a.filename.tolist():
    # take out cases we don't want
    exprsCEU = exprsCEU.drop(i, axis = 1)
(exprsCEU.columns == sampleinfoCEU.filename)

average = exprsCEU.sub(exprsCEU.mean(axis = 1), axis = 0)
average.head()

U,s,Vh = scipy.linalg.svd(average)
V = Vh.T
PC1 = V[:,0]
PC1

plt.hist(PC1, bins = 25)

V = Vh.T
plt.scatter(sampleinfoCEU['elapsedInDays'].astype(int), PC1)
plt.show()
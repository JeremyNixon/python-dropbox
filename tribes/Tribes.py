
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt



data = pd.read_csv('Parking_meters.csv')




print "Total meters in the data set = %i" %len(data)

smart = data[data['SMART_METE'] == 'Y']
print "Total smart meters in the data set = %i" %len(smart)

smart_geary = smart[smart['STREETNAME'] == 'GEARY BLVD']
print "Number of smart meters on Geary Blvd = %i" %len(smart_geary)




data1 = data
data1['POST_ID_COUNT'] = 1
by_streetname = data1.groupby(['STREETNAME'],as_index=False).sum()
print len(by_streetname)
by_streetname[:5]




Counter(data['STREETNAME']).most_common(5)




print by_streetname['POST_ID_COUNT'].mean()
print by_streetname['POST_ID_COUNT'].median()
print by_streetname['POST_ID_COUNT'].max()
print by_streetname['POST_ID_COUNT'].min()




data[:5]




q8 = pd.read_csv("Pub Inventory Analyst Sim - Q 8 to 11 (2).csv", header=-1)
q8[:5]




arr = []
for i in q8[0]:
    if i[-1:] == '*':
        arr.append(i[:-1])
    else:
        arr.append(i)




q8[0] = arr
q8[:5]




#Only run this if you want to create a new csv with the set of links free from asterix
q8.to_excel("no_asterix.xlsx")




q9a = pd.read_csv("q9a.csv")
q9b = pd.read_csv("q9b.csv")
merged = pd.merge(q9a,q9b,how="inner",on="Unnamed: 0")
m = pd.DataFrame()
m["Domain"] = merged["Unnamed: 0"]
m["Stock Price"] = merged["Stock Price_x"]
m["Volume"] = merged["Volume_x"]
m["EPS"] = merged["EPS_x"]
m


# Only run if you want to create a csv with the merged dataframe
#m.to_csv("Q9 Merged.csv")


q10 = pd.read_csv("Pub Inventory Analyst Sim - Q 8 to 11 (2).csv", header=-1)
print "Number of elements in the web url array is %i " %len(q10)


Counter(q10[0])


print "Number of instances of 'www.espn.com*' is 490"


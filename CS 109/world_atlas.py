import requests
import StringIO
import zipfile
import csv
url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
countries = pd.read_csv(url, sep = ',')
countries.head(10)

url = 'https://spreadsheets.google.com/pub?key=phAwcNAVuyj1jiMAkmq1iMg&gid=0&output=csv'
income = pd.read_csv(url, sep = ',')
income.head(10)

transposed_income = income.set_index(['gdp pc test']).transpose()
transposed_income.head()

income = income.dropna()
income['2000'].hist(bins=30, color = 'black')
plt.xlabel('Income')
plt.ylabel('Number of countries')

def mergeByYear(year):
    merged_df = countries.merge(income, left_on = 'Country', right_on = 'gdp pc test')
    final_df = merged_df.iloc[:, (0,1,(year-1800+3))]
    return final_df
mergeByYear(2010)

mergeByYear(2012).hist('2012', by='Region', bins=30, xrot=45)
plt.xlabel('Income per person')
plt.show()

mergeByYear(2007).hist('2007', by='Region', bins=30, xrot=45)
plt.xlabel('Income per person')
plt.show()

mergeByYear(2002).hist('2002', by='Region', bins=30, xrot=45)
plt.xlabel('Income per person')
plt.show()

mergeByYear(1997).hist('1997', by='Region', bins=30, xrot=45)
plt.xlabel('Income per person')
plt.show()

mergeByYear(1992).hist('1992', by='Region', bins=30, xrot=45)
plt.xlabel('Income per person')
plt.show()
from flask import Flask
app = Flask(__name__)

@app.route("/")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# For this assignment, we need to load in the following modules
import requests
import StringIO
import zipfile
import scipy.stats 

def getZIP(zipFileName):
    r = requests.get(zipFileName).content
    s = StringIO.StringIO(r)
    zf = zipfile.ZipFile(s, 'r') # Read in a list of zipped files
    return zf

url = 'http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip'
zf = getZIP(url)
print zf.namelist()

if __name__ == "__main__":
    app.run()
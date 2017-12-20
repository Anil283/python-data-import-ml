import numpy as np
import urllib.request

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

rawdata = urllib.request.urlopen(url)

#filename = "pima-indians-diabetes.csv"
#rawdata = open(filename, 'rt')

data = np.loadtxt(rawdata, delimiter = ",")

print("The dimensions (rows * columns) of the data are: ", data.shape)
print(data)

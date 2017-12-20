#Code for loading the Pima Indians Diabetes

from csv import reader

#List for loading the dataset
dataset = list()

#Convert String values to Float
def conv_str_to_float(dataset, col):
  for row_1 in dataset:
     row_1[col] =  float(row_1[col].strip())

with open('pima-indians-diabetes.csv') as datafile:
    rowreader = reader(datafile)

    for row in rowreader:
#      print (row)

       dataset.append(row)

    print("\n Number of Records in the file : ", len(dataset)) 
    print("\n Number of Columns in the dataset : ", len(dataset[0]))

    print("\n First Record (String Format): ", dataset[0]) 
    print("\n Last Record (String Format): ",  dataset[-1])

    for i in range(len(dataset[0])):
      conv_str_to_float(dataset, i)

    print("\n Changed (String to Float) First Record: ", dataset[0])    
    print("\n Changed (String to Float) Last Record: ",  dataset[-1])
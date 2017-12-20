import pandas

filename = "iris.csv"

names = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Class']

data = pandas.read_csv(filename, names=names)

print(data.shape)
print(data)
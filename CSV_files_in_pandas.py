import pandas

dataframes = pandas.read_csv('Python_Pandas/Historicalinvesttemp.csv')# Datasets download from kaggle
print(dataframes)

print(dataframes.loc[10:16])
print(dataframes.loc[[10,16]])


# head and tail
print(dataframes.head())# head prints first 5 rows
print(dataframes.head(7))# head(7) prints first 7 rows as its specifically said
print(dataframes.tail())# Tail prints last 5 rows
print(dataframes.tail(7))# Tail prints last 7 rows
print(dataframes.info())# Prints the information
# import relevant modules
import pandas

dataframes = pandas.read_csv('Python_Pandas/Book1.csv')
print(dataframes)

#  removes all the empty entries
print(dataframes.dropna())

# to fill the empty entries
dataframes['Year'] = dataframes['Year'].fillna(1933)
# 
# dataframes['Stocks'] = dataframes['Stocks'].fillna(10)
# dataframes['T.bills'] = dataframes['T.bills'].fillna(20)
# dataframes['T.bonds'] = dataframes['T.bonds'].fillna(30)
# print(dataframes)
# print(dataframes.fillna({'Stocks':10}, inplace = True)) # not working need to check
# print(dataframes.fillna(10))

# Mean and replacing value with mean 
mean = dataframes['Stocks'].mean()
print(mean)
dataframes['Stocks'] = dataframes['Stocks'].fillna(mean)
print(dataframes)

# Mean and replacing value with mean 
mode = dataframes['Stocks'].mode()[0]
print(mode)
dataframes['T.bills'] = dataframes['T.bills'].fillna(mode)
print(dataframes)

# Mean and replacing value with mean 
median = dataframes['Stocks'].median()
print(median)
dataframes['T.bonds'] = dataframes['T.bonds'].fillna(median)
print(dataframes)


#replacing the index value of 4  in stocks
dataframes.loc[4,'Stocks'] = 7.111111
print(dataframes)


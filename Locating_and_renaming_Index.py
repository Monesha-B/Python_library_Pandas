# import relevant modules

import pandas


# datasets are multi dimentional
#Pandas DataFrame is a 2-D data structure in which the data is organized in form of rows and columns
# "Dataset" is a more general term that refers to a collection of data. 
# It can include data in various formats and structures, 
# not necessarily confined to a tabular structure like a data frame.
# creating a datasets for the cars_Showroom with its stock availability
my_datasets = {
  "Car_Brands": ['Audi','Mini_cooper','BMW', 'Range_Rover'],
  "In-Stock": [12,10,8,14]
}

#load data into a DataFrame object:
my_dataframes = pandas.DataFrame(data = my_datasets, index= [1,2,3,4])

print(my_dataframes) 
# to print specific dataset
# print(my_dataframes.loc[[3]])-->can add multiple index and print(my_dataframes.loc[3]) makes difference in the listing

# to locating the datadrames '.loc is used 
print(my_dataframes.loc[3]) 
print(my_dataframes.loc[[3]])
print(my_dataframes.loc[[2,3]])
print(my_dataframes.loc[1:3]) #slicing - print dataframe from 1 to 3


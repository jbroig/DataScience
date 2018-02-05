import pandas 
import numpy as np

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    
    #YOUR CODE GOES HERE
    print(np.sum(baseball['weight']))
    print(np.mean(baseball['weight']))
    
    #Extraemos la media de la columna 'weight'
    avg = np.mean(baseball['weight'])
    
    #llenamos los campos vacíos o nulos de la columna 'weight' con la media mediante la funcion pantas.fillna(value)
    baseball['weight'] = baseball['weight'].fillna(avg)

    return baseball
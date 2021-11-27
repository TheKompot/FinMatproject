import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2021, 1, 1)
end  = datetime.datetime(2021, 11, 1)

def getStocks(stock_list:list, start:datetime, end:datetime)->pd.DataFrame:
    '''
    Returns a dataframe with Adj Close of all stocks in stocks_list

    Parameters:
    ----------
    stock_list:list
        list with stock codes
    start:datetime
        starting date
    end:datetime
        ending date

    Returns:
    -------
    pd.DataFrame
        returning dataframe
    '''
    output = pd.DataFrame()

    for stock in stock_list:
        try:
            output[stock] = web.DataReader(stock, 'yahoo', start, end)['Adj Close']
        except Exception as e:
            print(stock,e)

            
    return output.copy()

class GenAlg:

    def __init__(self, population_size,number_of_stocks, k_crossover, mutation_prob):
        self.population_size = population_size
        self.k_crossover = k_crossover
        self.mutation_prob = mutation_prob
        self.number_of_stocks = number_of_stocks

        self.random_pop()
    
    def random_pop(self):
        self.population = np.random.rand(self.population_size,self.number_of_stocks)
        for  i in range(self.population.shape[0]):
            self.population[i,] = self.normalize(self.population[i,])
    
    def normalize(self,vector):
        sum_of_vector = sum(vector)
        for i in range(len(vector)):
            vector[i] =  vector[i]/sum_of_vector
        return vector

# g = GenAlg(5, 10, 0, 0)
# for i in g.population:
#     print(sum(i))
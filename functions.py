import pandas as pd
import numpy as np
import datetime
import random
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

    def __init__(self, population_size, k_crossover, mutation_prob, rates, sigma):
        self.population_size = population_size
        self.k_crossover = k_crossover
        self.mutation_prob = mutation_prob
        self.number_of_stocks = len(rates)

        self.rates = rates.copy()
        self.sigma = sigma.copy()

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
    
    def evaluate(self):
        best_fitness = None
        best = None
        for vector in self.population:
            f = self.fitness(vector)
            if best is None or f > best_fitness:
                best = vector
                best_fitness = f
        return best_fitness,best

    def fitness(self,vector):
        rate = np.sum(vector * self.rates)
        volatility = np.sqrt(np.dot(vector.T,np.dot(self.sigma,vector)))

        return rate/volatility

    def get_lucky_one(self):
        random_num = random.randrange(len(self.population))
        return self.population[random_num,:]
    
    def select_parents(self,lucky_one):
        if lucky_one is not None:
            pop = np.ones(shape=(self.population_size-1,self.number_of_stocks))
            i = 0
            for vec in self.population:
                if not (vec == lucky_one).all():
                    pop[i,:] = vec
                    i+=1
        else:
            pop = self.population.copy()

        return pop

    def solve(self,max_generations, goal):
        
        best_fit, best = self.evaluate()
        
        for _ in max_generations:
            if best_fit > goal:
                break

            lucky_one = None
            if len(self.population)%2 == 1:
                lucky_one = self.get_lucky_one()

            parents = self.select_parents(lucky_one)

            children = self.create_children(parents)

            if lucky_one is not None:
                lucky_one = lucky_one.reshape((1,len(lucky_one)))
            self.population = np.concatenate((lucky_one,parents,children),axis=0)

            best_fit, best = self.evaluate()
        return best,best_fit


# wanted_stocks = ['GOOG', 'SPG', 'GOOGL', 'MSFT', 'GD', 'ACN', 'COP', 'F', 'BAC', 'GS',
#                 'NVDA', 'AIG', 'MS', 'WFC', 'ORCL', 'XOM', 'TGT', 'LOW', 'EXC', 'COST',
#                 'AXP', 'BK', 'JPM', 'COF', 'CSCO', 'DHR', 'UNH', 'CVS', 'LLY', 'CVX',
#                 'MET', 'AMT', 'CRM', 'BLK', 'RTX', 'MCD', 'TMO', 'LIN', 'ADBE', 'EMR',
#                 'USB', 'UPS', 'TSLA', 'PFE', 'PM']
# stocks = pd.read_csv('data/sap100_data_08112021.csv',index_col=0).loc[:,wanted_stocks]
# returns = stocks/stocks.shift(1)-1
# rates = returns.mean() * 252
# sigma = returns.cov() * 252
# g = GenAlg(5, 10, 0, rates,sigma)
# v = g.get_lucky_one()
# print('lucky one: ',v)
# print(v in g.select_parents(v))
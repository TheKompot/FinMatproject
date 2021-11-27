import pandas as pd
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
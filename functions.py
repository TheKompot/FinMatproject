import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

def validate(weights:np.array,axis:'plt.Axis',label:str):
    data = pd.read_csv('data/validation_data.csv', index_col=0, parse_dates=True)
    stocks = data/data.shift(1)

    balance = pd.Series(weights * 100000,index = data.columns)
    portfolio = pd.DataFrame(balance)

    for index,row in stocks.iloc[1:,:].iterrows():
        new_balance = row * balance
        portfolio = pd.concat([portfolio,new_balance],axis=1)
        balance = new_balance
    portfolio.columns = stocks.index
    portfolio = portfolio.T
    portfolio = pd.DataFrame(portfolio.sum(axis=1))
    axis.plot(portfolio.index,portfolio[0],label=label)

def plot_sectors(weights:np.array):
    data_file = 'data/s&p100.xlsx'
    sap100 = pd.read_excel(data_file)
    wanted_stocks = ('GOOG', 'SPG', 'GOOGL', 'MSFT', 'GD', 'ACN', 'COP', 'F', 'BAC', 'GS',
       'NVDA', 'AIG', 'MS', 'WFC', 'ORCL', 'XOM', 'TGT', 'LOW', 'EXC', 'COST',
       'AXP', 'BK', 'JPM', 'COF', 'CSCO', 'DHR', 'UNH', 'CVS', 'LLY', 'CVX',
       'MET', 'AMT', 'CRM', 'BLK', 'RTX', 'MCD', 'TMO', 'LIN', 'ADBE', 'EMR',
       'USB', 'UPS', 'TSLA', 'PFE', 'PM')

    sap100 = sap100[sap100['Symbol'].isin(wanted_stocks)]
    
    data = pd.DataFrame([weights,wanted_stocks]).T.rename(columns={1:'Symbol',0:'w'})

    data_sectors = pd.DataFrame((data.merge(sap100,on='Symbol').groupby('Sector')['w'].sum())).reset_index()

    fig = px.pie(data_sectors, values = 'w', names= 'Sector',title='% of capital by sector')
    fig.show()

def custom_plot(x,y1,y2,x_title,y1_title,y2_title):
    fig = go.Figure()
#mutation prob = 0.1, pop size 100
    fig.add_trace(go.Scatter(x=x, y=y1, name=y1_title, yaxis="y1"))
    fig.add_trace(go.Scatter(x=x, y=y2, name=y2_title, yaxis="y2"))
    fig.update_layout(
        xaxis=dict(title=x_title),
        yaxis=dict(
            title=y1_title,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis2=dict(
            title=y2_title,
            titlefont=dict(
                color="red"
            ),
            tickfont=dict(
                color="red"
            ),
            anchor="free",
            overlaying="y",
            side="right",
            position=1
        ))
    fig.show()
    
from Binance.BinanceClient import awais26_client
import pandas as pd

def get_aggregated_trades(ticker):
    json_data = awais26_client.get_aggregate_trades(symbol=ticker)
    tradesDF = pd.json_normalize(json_data)
    tradesDF['T'] = tradesDF['T'].astype("datetime64[ms]") 
    tradesDF.columns=['Id', 'Price', 'Quantity', 'FirstTradeId', 'LastTradeId', 'Date', 'IsBuyerMaker', 'IsBestPriceMatch']    

    return tradesDF.tail(20)

def get_historical_trades(ticker):
    json_data = awais26_client.get_historical_trades(symbol=ticker)
    tradesDF = pd.json_normalize(json_data)
    tradesDF['time'] = tradesDF['time'].astype("datetime64[ms]") 

    # tradesDF.columns=['Id', 'Price', 'Quantity', 'FirstTradeId', 'LastTradeId', 'Date', 'WasBuyerMaker', 'WasBestPriceMatch']    
    return tradesDF

def get_recent_trades(ticker):

    json_data = awais26_client.get_my_trades(symbol=ticker, limit=500)
    tradesDF = pd.json_normalize(json_data)
    cols = ['symbol', 'time', 'qty', 'price', 'quoteQty' ,'commission', 'commissionAsset', 'isBuyer', 'isMaker', 'isBestMatch']
    tradesDF = tradesDF[cols]
    tradesDF['time'] = pd.to_datetime(tradesDF['time'], unit='ms')
    tradesDF['time'] = tradesDF.time.dt.tz_localize('UTC').dt.tz_convert('Europe/Berlin')
    # tradesDF['time'] = pd.to_datetime(tradesDF['time'], unit='ms').dt.normalize()
    tradesDF.set_index('time', inplace=True)
    
    return tradesDF


def get_recent_trade_sum(ticker):

    json_data = awais26_client.get_my_trades(symbol=ticker)
    tradesDF = pd.json_normalize(json_data)
    tradesDF['time'] = pd.to_datetime(tradesDF['time'], unit='ms')
    tradesDF['time'] = tradesDF.time.dt.tz_localize('UTC').dt.tz_convert('Europe/Berlin')
    cols = ['symbol', 'time', 'qty', 'price', 'quoteQty', 'commission', 'commissionAsset', 'isBuyer', 'isMaker']
    groupbyCols = ['time','isBuyer', 'isMaker']
    tradesDF = tradesDF[cols]
    tradesDF[['qty', 'quoteQty', 'price', 'commission']] = tradesDF[['qty', 'quoteQty', 'price', 'commission']].apply(pd.to_numeric, errors='ignore')
    tradesDF['time'] = tradesDF['time'].dt.date
    
    tradesDF = tradesDF.groupby(groupbyCols, as_index=False)[['qty','price', 'quoteQty']].agg(
        {
            'qty': 'sum',
            'price' : 'mean',
            'quoteQty': 'sum'
        }
    )
    return tradesDF
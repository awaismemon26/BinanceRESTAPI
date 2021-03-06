#%%
from Binance.BinanceClient import awais26_client, awais100_client
import numpy as np
from pandas import DataFrame as dataframe
import pandas as pd

#%%
def get_awais26_current_balance():    

        allAssetsJson = awais26_client.get_account()     
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])         
        allAssetsDF['total_balance'] = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) 
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.total_balance == 0.00000000].index)
        allAssetsDF['asset'] = allAssetsDF['asset'].astype(str) + 'BTC'
        allAssetsDF['asset'] = np.where(allAssetsDF['asset']=='USDTBTC', 'BTCUSDT', allAssetsDF['asset'])
        allAssetsDF.set_index('asset', inplace=True)
        allAssetsDF[['free', 'locked', 'total_balance']] = allAssetsDF[['free', 'locked', 'total_balance']].astype('float64')
        return allAssetsDF
#%%
def get_awais100_current_balance():
        
        allAssetsJson = awais100_client.get_account()     
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])          
        totalBalance = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) 
        allAssetsDF['total_balance'] = totalBalance 
        
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.total_balance == 0.00000000].index)
        allAssetsDF['asset'] = allAssetsDF['asset'].astype(str) + 'BTC'
        allAssetsDF['asset'] = np.where(allAssetsDF['asset']=='USDTBTC', 'BTCUSDT', allAssetsDF['asset'])
        allAssetsDF.set_index('asset', inplace=True)
        allAssetsDF[['free', 'locked', 'total_balance']] = allAssetsDF[['free', 'locked', 'total_balance']].astype('float64')
        return allAssetsDF
#%%
def get_btc_value():
        btc_usdt_price = awais26_client.get_symbol_ticker(symbol='BTCUSDT')
        cleanDF = dataframe(btc_usdt_price, index=[0])
        cleanDF.set_index('symbol', inplace=True)
        cleanDF = float(cleanDF['price'][0])
        return cleanDF
# %%
def get_all_ticker_symbols():
        prices = awais26_client.get_all_tickers()
        pricesDF = dataframe(prices)
        pricesDF.set_index('symbol', inplace=True)
        return pricesDF
# %%
def get_awais26_merged_usdt_equivalent_balances():
        prices = get_all_ticker_symbols()
        balances = get_awais26_current_balance()
        joinedDF = balances.join(prices)

        joinedDF['btc_equivalent'] = joinedDF['price'].astype(float) * joinedDF['total_balance'].astype(float)
        joinedDF['usdt_equivalent'] = joinedDF['btc_equivalent'].multiply(float(get_btc_value()))
        
        for index, row in joinedDF.iterrows():
                if index == 'BTCUSDT':
                        joinedDF.at[index, 'usdt_equivalent'] = joinedDF.at[index, 'total_balance']
                        joinedDF.at[index, 'btc_equivalent'] = joinedDF.at[index, 'total_balance']
        
        joinedDF = joinedDF[joinedDF.usdt_equivalent > 1]
        joinedDF[['free', 'locked', 'total_balance', 'price', 'btc_equivalent', 'usdt_equivalent']] = joinedDF[['free', 'locked', 'total_balance', 'price', 'btc_equivalent', 'usdt_equivalent']].astype('float64')
        return joinedDF
#%%
def get_awais100_merged_usdt_equivalent_balances():
        prices = get_all_ticker_symbols()
        balances = get_awais100_current_balance()
        joinedDF = balances.join(prices)
        joinedDF['btc_equivalent'] = joinedDF['price'].astype(float) * joinedDF['total_balance'].astype(float)
        joinedDF['usdt_equivalent'] = joinedDF['btc_equivalent'].multiply(float(get_btc_value()))
        for index, row in joinedDF.iterrows():
                if index == 'BTCUSDT':
                        joinedDF.at[index, 'usdt_equivalent'] = joinedDF.at[index, 'total_balance']
                        joinedDF.at[index, 'btc_equivalent'] = joinedDF.at[index, 'total_balance']
        joinedDF = joinedDF[joinedDF.usdt_equivalent > 1]
        return joinedDF
# %%
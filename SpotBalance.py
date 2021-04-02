#%%
from binance.client import Client
from datetime import datetime 
from pandas import DataFrame as dataframe
import pandas as pd
from APICredentials import PKey, SKey, PKey_awais100, SKey_awais100

awais26_client = Client(PKey, SKey)
awais100_client = Client(PKey_awais100, SKey_awais100)

#%%
def get_awais26_current_balance():    

        allAssetsJson = awais26_client.get_account()     
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])         
        totalBalance = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) 
        allAssetsDF['TotalBalance'] = totalBalance  
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.TotalBalance == 0.00000000].index)
        return allAssetsDF

#%%
def get_awais100_current_balance():
        
        allAssetsJson = awais100_client.get_account()     
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])          
        totalBalance = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) 
        allAssetsDF['TotalBalance'] = totalBalance 
        
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.TotalBalance == 0.00000000].index)
        return allAssetsDF

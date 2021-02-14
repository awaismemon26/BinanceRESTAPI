from binance.client import Client
import Credentials.APIKeys as keys
from datetime import datetime 
from pandas import DataFrame as dataframe
import pandas as pd
import json

awais26Client = Client(keys.PKey, keys.SKey)
awais100Client = Client(keys.PKey_awais100, keys.SKey_awais100)

def GetAwais26CurrentBalanceDF():    

        allAssetsJson = awais26Client.get_account()     # Awais26 Account
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])          ## Data is coming in Json then converted by json_normalize method
        totalBalance = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) # Total Balance
        allAssetsDF['TotalBalance'] = totalBalance  # Added newly created totalbalance to our Dataframe
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.TotalBalance == 0.00000000].index)
        return allAssetsDF


def GetAwais100CurrentBalanceDF():

        allAssetsJson = awais100Client.get_account()     # Awais100 Account
        allAssetsDF = pd.json_normalize(allAssetsJson["balances"])          ## Data is coming in Json then converted by json_normalize method
        totalBalance = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) # Total Balance
        allAssetsDF['TotalBalance'] = totalBalance  # Added newly created totalbalance to our Dataframe
        
        allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.TotalBalance == 0.00000000].index)
        return allAssetsDF

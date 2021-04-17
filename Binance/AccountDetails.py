#%%
from Binance.BinanceClient import awais26_client
from pandas import DataFrame as dataframe
import pandas as pd

#%%
def get_awais26_account_snapshot_spot():    

        json_data = awais26_client.get_account_snapshot(type='SPOT')
        snapshots = json_data['snapshotVos']
        
        snapshotsDF = pd.json_normalize(snapshots)
        # flatJson = flatten_json(snapshotsDF['data.balances'])
        snapshotsDF['updateTime'] = snapshotsDF['updateTime'].astype("datetime64[ms]") 
        
        
        # allAssetsDF['updateTime'] = allAssetsDF['updateTime'].astype(int).apply(lambda x: datetime.datetime.fromtimestamp("%H:%M:%S"))
        # allAssetsDF['total_balance'] = allAssetsDF['free'].astype(float) + allAssetsDF['locked'].astype(float) 
        # allAssetsDF = allAssetsDF.drop(allAssetsDF[allAssetsDF.total_balance == 0.00000000].index)
        # allAssetsDF['asset'] = allAssetsDF['asset'].astype(str) + 'BTC'
        # allAssetsDF['asset'] = np.where(allAssetsDF['asset']=='USDTBTC', 'BTCUSDT', allAssetsDF['asset'])
        # allAssetsDF.set_index('asset', inplace=True)
        # allAssetsDF[['free', 'locked', 'total_balance']] = allAssetsDF[['free', 'locked', 'total_balance']].astype('float64')
        return snapshotsDF

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

print(get_awais26_account_snapshot_spot())
# %%

from binance.client import Client
import os

__PKey = os.environ.get('BINANCEAPI_AWAIS26_PKEY')
__SKey = os.environ.get('BINANCEAPI_AWAIS26_SKEY')
__PKey_awais100 = os.environ.get('BINANCEAPI_AWAIS100_PKEY')
__SKey_awais100 = os.environ.get('BINANCEAPI_AWAIS100_SKEY')

awais26_client = Client(__PKey, __SKey)
awais100_client = Client(__PKey_awais100, __SKey_awais100)
from flask_restful import Resource
import Binance.SpotBalance as SpotBalance
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
import os

username = os.environ.get('BINANCEAPI_USERNAME')
password = os.environ.get('BINANCEAPI_PASSWORD')

USER_DATA = {
    username: generate_password_hash(password)
}

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in USER_DATA and \
            check_password_hash(USER_DATA.get(username), password):
        return username

class SpotWallet(Resource):
    @auth.login_required
    def get(self, account_id):
        if account_id == '1':
            get_balanceDF = SpotBalance.get_awais26_merged_usdt_equivalent_balances()
            json_object = get_balanceDF.to_json(orient='records')  
            return json_object
        elif account_id == '2':
            get_balanceDF = SpotBalance.get_awais100_merged_usdt_equivalent_balances()
            json_object= get_balanceDF.to_json(orient = "records")
            return json_object
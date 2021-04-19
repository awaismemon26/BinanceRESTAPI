from flask_restful import Resource, reqparse
import Binance.Trades as trades
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

class GetRecentTradesSummary(Resource):
    @auth.login_required
    def get(self, account_id):
        if account_id == '1':
            parser = reqparse.RequestParser()
            parser.add_argument('symbol', type=str)
            args = parser.parse_args(strict=True)
            get_tradeDF = trades.get_recent_trade_sum(args['symbol'])
            json_object = get_tradeDF.to_json(orient='records')  
            return json_object
        elif account_id == '2':
            return 404
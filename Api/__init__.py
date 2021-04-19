from Api.AccountEndpoint import AccountByID, AccountsList
from Api.SpotEndpoint import SpotWallet
from Api.TradeEndpoint import GetRecentTradesSummary
from flask import Flask
from flask_restful import Api
import os

app = Flask(__name__)
api = Api(app, "/api/v1")

api.add_resource(AccountsList, '/accounts')
api.add_resource(AccountByID, '/accounts/<account_id>')
api.add_resource(SpotWallet, '/accounts/<account_id>/spot')
api.add_resource(GetRecentTradesSummary, '/accounts/<account_id>/summTrades')

if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=PORT)
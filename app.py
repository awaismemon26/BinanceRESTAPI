from APIResources.AccountsList import AccountByID, AccountsList
from APIResources.SpotWallet import SpotWallet
from flask import Flask
from flask_restful import Api

app = Flask(__name__) # Instance of the class
api = Api(app, "/api/v1")

api.add_resource(AccountsList, '/accounts')
api.add_resource(AccountByID, '/accounts/<account_id>')
api.add_resource(SpotWallet, '/accounts/<account_id>/spot')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
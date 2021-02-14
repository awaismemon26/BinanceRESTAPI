from flask import json
from flask_restful import Resource, Api
from pandas import DataFrame as dataframe
import SpotBalance
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
import Credentials.Login

USER_DATA = {
    Credentials.Login.username: generate_password_hash(Credentials.Login.password)
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
            getBalanceDF = SpotBalance.GetAwais26CurrentBalanceDF()
            json_object = getBalanceDF.to_json(orient='records') 
            # df_json_pretty = json.dumps(json.loads(json_object), indent=4)
            return json_object
        elif account_id == '2':
            getBalanceDF = SpotBalance.GetAwais100CurrentBalanceDF()
            json_object= getBalanceDF.to_json(orient = "records")
            return json_object
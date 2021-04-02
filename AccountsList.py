from flask import jsonify
from flask_restful import Resource, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash
from LoginCredentials import username, password

listOfAccounts = [
    {'id': '1', 'name': 'Awais26'},
    {'id': '2', 'name': 'Awais100'}]

USER_DATA = {
    username: generate_password_hash(password)
}

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in USER_DATA and \
            check_password_hash(USER_DATA.get(username), password):
        return username


class AccountsList(Resource):    
    @auth.login_required
    def get(self):
        return jsonify(listOfAccounts)    


class AccountByID(Resource):
    @auth.login_required
    def get(self, account_id):
        formatedAccount_id = '{0}'.format(account_id)
        for account in listOfAccounts:
            if account['id'] == formatedAccount_id:
                return jsonify(account)
            
        return abort(404)



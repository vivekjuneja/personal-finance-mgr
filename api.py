from flask import Flask
from flask import request
from backend import Backend
from source import Source
from app import Master
from payment import Payment
import datetime
webapp = Flask(__name__)

backend = Backend()

@webapp.route("/accounts", methods=['POST'])
def createAccount():
	app1=Master()
	app1.name=request.json['name']
    	return str(backend.addApp(app1))

@webapp.route("/accounts/<accountid>", methods=['GET'])
def getAccount(accountid):
        return str(backend.getApp(accountid))

@webapp.route("/accounts/<accountid>/sources", methods=['POST'])
def addSource(accountid):
	source = Source(request.json['code'], request.json['name'], request.json['init'], request.json['currency'])
	app1=backend.getApp(accountid)
	app1.addSource(source)
    	backend.setApp(app1.id, app1)
    	return str(source.code)


@webapp.route("/accounts/<accountid>/sources/<sourcecode>", methods=['GET'])
def getSource(accountid, sourcecode):
    source = backend.getSource(accountid, sourcecode)
    return source.name

@webapp.route("/accounts/<accountid>/sources/<sourcecode>/pay", methods=['POST'])
def pay(accountid, sourcecode):
    source = backend.getSource(accountid, sourcecode)
    payment = Payment(request.json['amount'],request.json['reason'], datetime.datetime.now().time())
    app1=backend.getApp(accountid)
    app1.performTransaction(payment, source)
    backend.setApp(app1.id, app1)   
    return str(app1.id)


@webapp.route("/accounts/<accountid>/balance", methods=['GET'])
def getAccountBalance(accountid):
    app1=backend.getApp(accountid)
    return str(app1.getBalance())

@webapp.route("/accounts/<accountid>/sources/<sourcecode>/balance", methods=['GET'])
def getBankBalance(accountid, sourceid):
    return "Hello World! " + sourceid


if __name__ == "__main__":
    webapp.run()

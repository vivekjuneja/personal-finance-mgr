import app, source, payment, datetime

class Backend:

	counter=0

	def __init__(self):
		self.apps = {}

	def addApp(self, account):
		account.id = self.counter
		print "hello"
		self.apps[account.id] = account
		self.counter = self.counter + 1
		return account.id

	def getApp(self, id):
		print self.apps
		print "id " + id
		return self.apps[int(id)]

	def setApp(self, id, account):
		self.apps[id]=account
		return id

	def getSource(self, accountId, sourceCode):
		account = self.apps[int(accountId)]
		return account.getSource(sourceCode)

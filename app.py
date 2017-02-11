import source, ledger, payment
from datetime import datetime

class Master:

	def __init__(self, name=None):
		self.name = name
		self.sources = {}
		self.globalLedger = ledger.Ledger()
		self.paylist = {}	
		self.id = None	

	def addSource(self, source):
		self.sources[source.code]=source
		initPay = payment.Payment(source.balance, "Init", datetime.now().time(), source.code)
		self.globalLedger.addPayment(initPay)

	def performTransaction(self, payment, source):
		payment.source = source.code
		self.globalLedger.addPayment(payment)
		source.makeTransaction(payment)

	def getSource(self, sourceCode):
		return self.sources[sourceCode]

	def getSourceWithId(self, sourceId):
		return self.sources[sourceId]

	def getBalance(self):
		return self.globalLedger.calculateLedgerBalance()

	def printTransactions(self):
		self.globalLedger.printLedger()
		print ("=====================")
		for eachSource in self.sources:
			print ("%-33s %-10s" % (eachSource, self.sources[eachSource].getBalance()))   
		
		print ("%-33s %-10s" % ("TOTAL", self.getBalance()))   


	def registerPay(self, pay, date, source):
		pay.source = source
		self.paylist[date]=pay

	def executeScheduledPay(self):
		for date in self.paylist:
			if date == datetime.now().date():
				print 'hello'
				self.performTransaction(self.paylist[date], self.paylist[date].source)









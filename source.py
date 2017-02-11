import ledger, payment, datetime

class Source:

	counter=0

	def __init__(self, sourceCode, sourceName, initBalance, currency):
		self.id = self.counter
		self.code = sourceCode
		self.name = sourceName
		self.balance = initBalance
		self.currency = currency
		self.ledger = ledger.Ledger()
		initPay = payment.Payment(initBalance, "Init", datetime.datetime.now().time())
		initPay.source = sourceCode
		self.makeTransaction(initPay)
		self.counter = self.counter + 1

	def makeTransaction(self, payment):
		self.ledger.addPayment(payment)

	def getBalance(self):
		return self.ledger.calculateLedgerBalance()

	def printTransactions(self):
		self.ledger.printLedger()
		print ("=====================")		
		print ("%-33s %-10s" % (self.code, self.getBalance()))   








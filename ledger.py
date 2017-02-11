import payment, collections

class Ledger:

	def __init__(self):
		self.payments = collections.OrderedDict()

	def addPayment(self, payment):
		self.payments[payment.time]=payment

	def calculateLedgerBalance(self):
		total = 0
		for date in self.payments:
			total += self.payments[date].amount
		return total

	def printLedger(self):
		print ("%-10s %-20s %-10s %-10s %-10s" % ("SOURCE", "TIME", "REASON", "AMOUNT", "LOCATION"))   
		for date in self.payments:
			print ("%-10s %-20s %-10s %-10d %-10s" % (self.payments[date].source, self.payments[date].time, self.payments[date].reason, self.payments[date].amount, self.payments[date].reason))   




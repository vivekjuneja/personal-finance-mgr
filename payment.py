
class Payment:

	def __init__(self, amount, reason, time, source=None, location=None, currency="USD"):
		self.amount = amount
		self.reason = reason
		self.time = time
		self.location = location
		self.currency = currency
		self.source = source



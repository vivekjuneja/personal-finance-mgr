import source, payment, datetime

bankOne = bank.Bank("Woori", "Woori", 0, "KRW")
print (bankOne.bankName)
print (bankOne.balance)
print (bankOne.currency)

pay1 = payment.Payment(1000,"Demo", datetime.datetime.now().time() )
pay2 = payment.Payment(-500,"Demo", datetime.datetime.now().time() )

bankOne.makeTransaction(pay1)

bankOne.makeTransaction(pay2)

print("Balance: %d" % bankOne.getBalance())
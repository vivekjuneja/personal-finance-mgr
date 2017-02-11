import app, source, payment, datetime

bankOne = source.Source("Woori", "Woori", 0, "KRW")

bankTwo = source.Source("CITI", "CITI", 1000, "KRW")

app1=app.Master()
app1.addSource(bankOne)
app1.addSource(bankTwo)


pay1 = payment.Payment(1000,"Savings", datetime.datetime.now().time() )
pay2 = payment.Payment(-500,"Phone Bill", datetime.datetime.now().time() )

salaryPay = payment.Payment(6000,"Salary", datetime.datetime.now().time())


#app1.performTransaction(pay1, bankOne)
#app1.performTransaction(pay2, bankOne)
app1.performTransaction(salaryPay, bankTwo)

schedulePay = payment.Payment(-300,"Grocery", datetime.datetime.now().time())


datestr = '2017-02-11'
dateobj = datetime.datetime.strptime(datestr,'%Y-%m-%d').date()

app1.registerPay(schedulePay, dateobj, bankTwo)

app1.executeScheduledPay()



print("----")
#bankOne.printTransactions()
#print("----")
bankTwo.printTransactions()
print("----")
#app1.printTransactions()


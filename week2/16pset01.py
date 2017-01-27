balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    monthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = (balance - monthlyPayment)
    interest = unpaidBalance * annualInterestRate / 12
    balance = round(unpaidBalance + interest, 2)

print(balance)

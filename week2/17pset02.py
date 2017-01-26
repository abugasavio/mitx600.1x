
balance = 91
annualInterestRate = 0.2


def amount_end(monthlyPayment):
    currentBalance = balance

    for month in range(1, 13):
        unpaidBalance = (currentBalance - monthlyPayment)
        interest = unpaidBalance * annualInterestRate / 12
        currentBalance = round(unpaidBalance + interest, 2)
    return currentBalance, monthlyPayment


monthlyPayment = 10

while amount_end(monthlyPayment)[0] > 0:
    monthlyPayment += 10
    least_amount = amount_end(monthlyPayment)[1]
else:
    least_amount = monthlyPayment

print('Lowest Payment: ' + str(least_amount))

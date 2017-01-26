
balance = 91
annualInterestRate = 0.2


def amount_end(monthlyPayment):
    currentBalance = balance

    for month in range(1, 13):
        unpaidBalance = (currentBalance - monthlyPayment)
        interest = unpaidBalance * annualInterestRate / 12
        currentBalance = round(unpaidBalance + interest, 2)
    return currentBalance


lower_bound = balance // 12
upper_bound = int((balance * (1 + annualInterestRate) ** 12) // 12)
middle = (lower_bound + upper_bound) / 2


for amount in range(lower_bound, upper_bound):

    if amount_end(middle) > 0:
        upper_bound = middle
    else:
        lower_bound = middle

    middle = (lower_bound + upper_bound) / 2
    print(middle)


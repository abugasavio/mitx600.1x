
balance = 999999
annualInterestRate = 0.18


lower_bound = balance / 12
upper_bound = (balance * (1 + (annualInterestRate / 12)) ** 12) / 12
middle = (lower_bound + upper_bound) / 2


def amount_end(monthly_payment):
    current_balance = balance

    for month in range(1, 13):
        unpaid_balance = (current_balance - monthly_payment)
        interest = unpaid_balance * annualInterestRate / 12
        current_balance = round(unpaid_balance + interest, 2)
    return current_balance


while abs(amount_end(middle)) > 0.01:
    print(amount_end(middle))
    if amount_end(middle) > 0:
        lower_bound = middle
    else:
        upper_bound = middle

    middle = (lower_bound + upper_bound) / 2

print('Lowest Payment: ' + str(round(middle, 2)))


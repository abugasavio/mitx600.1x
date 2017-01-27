
balance = 3451
annualInterestRate = 0.2
amountEnd = 10

lower_bound = balance / 12
upper_bound = (balance + (1 * annualInterestRate) ** 12) / 12
middle = (lower_bound + upper_bound) / 2


def amount_end(monthly_payment):
    current_balance = balance

    for month in range(1, 13):
        unpaid_balance = (current_balance - monthly_payment)
        interest = unpaid_balance * annualInterestRate / 12
        current_balance = round(unpaid_balance + interest, 2)
    return current_balance


while amount_end(amountEnd) > 0:
        amountEnd += 10

print(amountEnd)


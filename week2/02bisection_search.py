"""
Using bisection search to approximate square root
"""
x = 25
epsilon = 0.01
num_of_guesses = 0
low = 0.0
high = max(1.0, abs(x))
ans = (high + low) / 2.0

while abs(ans**2 - abs(x)) >= epsilon:
    print('low=' + str(low) + 'high=' + str(high))
    num_of_guesses += 1
    if ans**2 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

if x < 0:
    ans = -ans

print('num_of_guesses' + str(num_of_guesses))
print(ans)

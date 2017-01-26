"""
Approximating the square root using exhaustive enumaration
"""

x = 25
epsilon = 0.1
step = epsilon**2
num_of_guesses = 0
ans = 0.0

print(abs(ans**2 - x))
print(step)

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    num_of_guesses += 1
print('Number of guesses: ' + str(num_of_guesses))
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print(str(ans) + ' is close to the square root of ' + str(x))

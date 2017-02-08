number = 25
epsilon = 1
step = 0.01
guess = 0

while abs(guess ** 2 - number) > epsilon:
    guess += step

print(guess)

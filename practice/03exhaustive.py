number = int(input("Enter number:"))
guess = 0

while guess ** 3 < abs(number):
    guess += 1

if guess ** 3 == number:
    print("Perfect cube", guess)
else:
    print(guess)

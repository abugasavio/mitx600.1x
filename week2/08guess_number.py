print('Please think of a number between 0 and 100!')
correct = False

high = 100
low = 0

guess = int((high + low) / 2)

valid_inputs = ['c', 'h', 'l']

while not correct:
    print('Is your secret number ' + str(guess) + '?')
    while True:
        status = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if status not in valid_inputs:
            print('Sorry, I did not understand your input.')
            print('Is your secret number ' + str(guess) + '?')
            continue
        break

    if status == 'c':
        correct = True
    elif status == 'l':
        low = guess
    elif status == 'h':
        high = guess
    guess = int((high + low) / 2)

print('Game over. Your secret number was: ' + str(guess))



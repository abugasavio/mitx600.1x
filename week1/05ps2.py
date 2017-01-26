s = 'jmeocobdobvjbb'

bob_count = 0

for index, letter in enumerate(s):
    if letter == 'b':
        try:
            o, b = s[index + 1], s[index + 2]
        except IndexError:
            pass
        else:
            if o == 'o' and b == 'b':
                bob_count += 1

print('Number of times bob occurs is: ' + str(bob_count))

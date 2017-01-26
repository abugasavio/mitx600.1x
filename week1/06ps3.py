
s = 'abcdefghijklmnopqrstuvwxyz'

n = s[0]

for index, letter in enumerate(s):

    if index == 0:
        continue
    if ord(letter) >= ord(s[index - 1]):
        n += letter
    else:
        n += ',' + letter

words = n.split(',')

# largest = 0

# for index, word in enumerate(words):

#     if len(word) > len(words[largest]):
#         largest = index

# print('Longest substring in alphabetical order is: ' + words[largest])

# Cleaner way to get the max
largest = max(words, key=len)

print('Longest substring in alphabetical order is: ' + largest)






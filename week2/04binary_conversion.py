# 8 == 1000

x = 19

result = ''

while x > 0:
    result += str(x % 2)
    x = x / 2

print(result)

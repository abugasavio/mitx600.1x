

def multi_iter(x, b):
    result = 0
    while b:
        result += x
        b -= 1
    return result

print(multi_iter(10,3))



def oddTuples(aTup):
    odd = ()
    for num, item in enumerate(aTup):
        if num % 2 == 0:
            odd += (item,)
    return odd
print(oddTuples((0, 15, 11, 6, 3, 0, 7, 14, 19)))
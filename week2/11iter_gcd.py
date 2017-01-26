def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smaller = a if a < b else b

    while smaller:
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        smaller -= 1


print(gcdIter(9, 12))

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle = len(aStr) // 2

    if not aStr or char > aStr[len(aStr) - 1]:
        return False

    if aStr[middle] == char:
        return True
    else:
        return isIn(char, aStr[:middle] if aStr[middle] > char else aStr[middle:])


print(isIn('q', 'abcd'))

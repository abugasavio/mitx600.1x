def palindrome(text):
    print(text)
    if len(text) < 1:
        return True
    else:
        return text[0] == text[-1] and palindrome(text[1:-1])
print(palindrome('bpoklklpb'))

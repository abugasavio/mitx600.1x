def how_many(aDict):
    total = 0
    for item in aDict.values():
        if type(item) in (list, tuple):
            total += len(item)
        else:
            total += 1
    return total

print(how_many({ 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['afds', 'fdsa']}))



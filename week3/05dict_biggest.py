def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    """
    # Your Code Here
    values = aDict.values()

    big = len(max(values, key=len))
    if not big:
        return

    for key, value in aDict.items():
        if len(value) == big:
            return key



print(biggest({'a': ['aardvark', 'fsadf'], 'b': ['baboon'], 'c': ['coati']}))

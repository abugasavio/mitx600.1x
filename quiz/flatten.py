def flatten(aList):
    """
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    """
    l = []
    for i in aList:
        if type(i) is list:
            l.extend(flatten(i))
        else:
            l.append(i)
    return l


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,[[[7]]]]
print(flatten(aList))
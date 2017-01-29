def product(listing):
    print(listing)
    if len(listing) == 2:
        return [listing[1] * listing[0]]
    else:
        l = [listing[0] * listing[1]]
        l.extend(product(listing[1:]))
        return l


print(product([1,2,3,4,4,5,4,3,9]))
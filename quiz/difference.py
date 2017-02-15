def f(l1, l2):
    return l1 + l2


def dict_interdiff(d1, d2):
    """
    :param d1: dict one whose keys are integers
    :param d2: dict two whose keys are integers
    :return: a tuple of a dictionary of intersection and a dictionary of differences
    """
    dict_inter = {}

    # intersection
    for key, item in d1.items():
        if key in d2.keys():
            dict_inter[key] = f(item, d2[key])

    # difference
    dict_diff = {}
    for key, item in d1.items():
        if key not in d2.keys():
            dict_diff[key] = item

    for key, item in d2.items():
        if key not in d1.keys():
            dict_diff[key] = item

    return dict_inter, dict_diff



d1 = {1: 30, 2: 20, 3: 30, 5: 80}
d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}

print(dict_interdiff(d1, d2))


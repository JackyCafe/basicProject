lt = {'Justin', 'caterpilar', 'openhome'}


def greater_than_6(elem):
    return len(elem) > 6


def less_than_5(elem):
    return len(elem) < 5


def has_i(elem):
    return 'i' in elem


def filter_lt(predicate, lt):
    result = []
    for elem in lt:
        if predicate(elem):
           result.append(elem)

    return result


print(filter_lt(greater_than_6, lt))
print(filter_lt(less_than_5, lt))
print(filter_lt(has_i, lt))

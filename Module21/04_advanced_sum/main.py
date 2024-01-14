def super_sum(*args):
    result = 0
    for elem in args:
        if isinstance(elem, (int, float)):
            result += elem
        else:
            for i, val in enumerate(elem):
                result += super_sum(val)
    return result


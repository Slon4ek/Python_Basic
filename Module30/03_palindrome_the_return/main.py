from collections import Counter


def can_be_poly(string):
    odd_count = sum(map(lambda x: x % 2 != 0, Counter(string).values()))
    if odd_count > 1:
        return False
    else:
        return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

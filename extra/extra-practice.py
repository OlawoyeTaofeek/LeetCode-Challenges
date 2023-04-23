# Permutation
def FindLength(value):
    count = 0
    for i in value:
        count += 1
    return count


def permutation(list1, list2):
    if FindLength(list1) != FindLength(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

print(permutation(['a', 'b', 'c'], ['c', 'a', 'b']))
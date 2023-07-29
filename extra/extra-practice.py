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

# Best Score
#Given a list, write a function to get first, second best scores from the list.

##List may contain duplicates.

#Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
#firstSecond(myList) # 90 87

def firstSecond(givenList):
    # TODO
    lst = list(set(givenList))
    lst.sort()
    return lst[-1], lst[-2]
print(firstSecond([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))
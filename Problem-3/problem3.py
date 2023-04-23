# Solution 1

def addTwoNumbers(l1, l2):
    x = ''.join(str(e) for e in l1)[::-1]
    y = "".join(str(a) for a in l2)[::-1]
    w = str(int(x)+int(y))[::-1]
    output = [int(j) for j in w ]
    return output

print(addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
print(addTwoNumbers(l1 = [0], l2 = [0]))
print(addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))


# Solution 2


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.value, end=' --> ')
        current = current.next
    # print('None')
        
        
print(printLinkedList(a))

def recursivePrint(head):
    if head == None:
        return   
    else:
        print(head.value, end=' --> ')
        return recursivePrint(head.next)
    
print(recursivePrint(a))

def linkedlistvalues(head):
    current = head 
    arr = []
    while current is not None:
        arr.append(current.value)
        current = current.next
    return arr


# # # print(linkedlistvalues(a))

def recursive(head):
    arr = []
    if head == None:
        return []
    else:
        arr.append(head.value)
        return arr + recursive(head.next)
    
print(recursive(a))


# Write a function, sumList, that takes in the head 
# of a linked list containing numbers as an argument. 
# The function should return the total sum of all values in the linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def SumOfLinkedList(head):
    current = head
    total_sum = 0
    while current != None:
        total_sum += current.value
        current = current.next
    return total_sum

print(SumOfLinkedList(a))


x = Node(38)
y = Node(4)
x.next = y
print(SumOfLinkedList(x))

z = Node(100)

print(SumOfLinkedList(z))

def SumLinkedListRecursively(head):
    if head == None:
        return 0
    total = head.value
    return total + SumLinkedListRecursively(head.next)
    
print(SumLinkedListRecursively(a))
x = Node(38)
y = Node(4)
x.next = y
print(SumLinkedListRecursively(x))


#Write a function, linkedListFind, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.
def linkedListFind(head, target):
    current = head
    if (current is None):
        return False
    i = 0
    while (current is not None):
        if current.value == target:
            print(f'The {target} is located at index {i}')
            return True
        current = current.next
        i = i + 1
    return False

def recursivePrint(head):
    if head == None:
        return   
    else:
        print(head.value, end=' --> ')
        return recursivePrint(head.next)
            
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
print(linkedListFind(a, -1))

print(recursivePrint(a))

def linkedListFindRecursively(head, target):
    if head == None:
        return False
    elif head.value == target:
        return True
    return linkedListFindRecursively(head.next, target)

print(linkedListFindRecursively(a, 3))



# Write a function, getNodeValue, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index. If there is no node at the given index, then return null.
def getNodeValue(head, index):
    current = head
    i = 0
    while current != None:
        if i == index:
            return current.value
        current = current.next
        i = i + 1
        
    return None

print(getNodeValue(a, 2))
def getNodeValueRecursively(head, index):
    if head == None:
        return None
    if index == 0:
        return head.value
    return getNodeValueRecursively(head.next, index-1)

print(getNodeValueRecursively(a, 2))


# Write a function, reverseList, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

def reverseLinkedList(head):
    current = head
    prev = None
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt   
        
    return prev



a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(recursivePrint(reverseLinkedList(a)))

def reverseLinkedListRecursively(head, prev=None):
    if head is None:
        return prev
    nxt = head.next
    head.next = prev 
    return reverseLinkedListRecursively(nxt, head)

print(recursivePrint(reverseLinkedListRecursively(a)))


#Write a function, zipperLists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list. Do this in-place, by mutating the original Nodes.

def zipperLists(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    i = 0
    
    while (current1 != None) and (current2 != None):
        if i % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        i = i + 1
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
        
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        
def linkedlistvalues(head):
    current = head 
    arr = []
    while current is not None:
        arr.append(current.value)
        current = current.next
    return ''.join([str(i) for i in arr])
        
def reverseList(head):
    prev = None
    current = head
    while (current != None):
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

def addTwoNumbers(l1, l2):
    ll1 = linkedlistvalues(reverseList(l1))
    ll2 = linkedlistvalues(reverseList(l2))
    results = str(int(ll1) + int(ll2))
    
    return results
        
def createLinkedListFromString(string):
    head = None
    prev = None

    for char in string:
        new_node = Node(char)

        if not head:
            head = new_node
        else:
            prev.next = new_node

        prev = new_node

    return head

def recursivePrint(head):
    if head == None:
        return   
    else:
        print(head.value, end=' --> ')
        return recursivePrint(head.next)

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

def linkedlistvalue(head):
    current = head 
    arr = []
    while current is not None:
        arr.append(current.value)
        current = current.next
    return [int(i) for i in arr]


l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)
print(linkedlistvalue(reverseList(createLinkedListFromString(addTwoNumbers(l1, l2)))))
print(7//10)
print(10%10)
print(7%10)

def remove(head, location):
    if location == 0:
        head = head.next
        head.next = head
    count = 0
    current =  head
    while current != None and count < location -1:
        current = current.next
        count = count + 1
        
    nextNode = current.next
    current.next = nextNode
    
    

    
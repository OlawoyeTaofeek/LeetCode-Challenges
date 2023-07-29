# # Solution 1: Considering it as Array or List

# # def addTwoNumbers(l1, l2):
# #     x = ''.join(str(e) for e in l1)[::-1]
# #     y = "".join(str(a) for a in l2)[::-1]
# #     w = str(int(x)+int(y))[::-1]
# #     output = [int(j) for j in w ]
# #     return output

# # print(addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
# # print(addTwoNumbers(l1 = [0], l2 = [0]))
# # print(addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))


# Solution 2
from locale import currency


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
    
        # Adding an element to linked list(Last)                 
    def add_to_llist(self, value):
        newNode = Node(value)
        node = self.head
        if node is None:
            self.head = newNode
            return 
        # Add to tail
        while True:
            if node.next is None:
                node.next = newNode
                break
            node = node.next
        
    def reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node is not None:
            nxt = curr_node.next
            # Change the direction of the node
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = nxt
            
        self.head = prev_node
        return self.head
    

l1 = LinkedList()
l1.add_to_llist(9)
l1.add_to_llist(9)
l1.add_to_llist(9)
l1.add_to_llist(9)
l1.add_to_llist(9)
l1.add_to_llist(9)
l1.add_to_llist(9)

l2 = LinkedList()
l2.add_to_llist(9)
l2.add_to_llist(9)
l2.add_to_llist(9)
l2.add_to_llist(9)
l1.reverse()
l2.reverse()

print([elem.value for elem in l1])
print([elem.value for elem in l2])
ll1 = ''.join([str(elem.value) for elem in l1])
ll2 = ''.join([str(elem.value) for elem in l2])
output = str(int(ll1) + int(ll2))

myLinkedList = LinkedList()

for elem in output:
    myLinkedList.add_to_llist(elem)
    
print(myLinkedList.reverse())
print([int(node.value) for node in myLinkedList])
    

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        
def printList(l):
    while l:
        print(l.value)
        l = l.next
        
        
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)


l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

print(printList(l1)) 

def addTwoNumbers(l1, l2):
    # Instantiate a node to take the values
    dummy = Node()
    current = dummy
    remainder = 0
    
    while l1 or l2 or remainder:
        ll1 = l1.value if l1 else 0
        ll2 = l2.value if l2 else 0
        
        # Calculate the sum of each node 
        total = ll1 + ll2 + remainder
        remainder = total // 10
        digits = total % 10
        
        # Create a new node with the calculated digit
        current.next = Node(digits)
        current = current.next
        
        # Move to the next nodes in l1 and l2
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

def linkedlistvalues(head):
    current = head 
    arr = []
    while current is not None:
        arr.append(current.value)
        current = current.next
    return arr

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)


l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

        
        
         
        
        
    
        
    

        
        
        
        
    


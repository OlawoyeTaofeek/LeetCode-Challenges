# Creating A Linked List

class Node:
    """
       Create a class to represent each node of the linked list:
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
    # def __repr__(self):
    #     return self.data
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        
# Instantiate the Linked List

singlyLinkedlist = SinglyLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedlist.head = node1
singlyLinkedlist.head.next = node2
singlyLinkedlist.tail = node2  


# lINKED LIST 
class Node2:
    """
       Create a class to represent each node of the linked list:
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
    
class  LinkedList:
    def __init__(self):
        self.head = None
        self.tail = 'None'
        
    def __repr__(self) -> str:
        node = self.head
        tail = self.tail
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append(tail)
        return " -> ".join(nodes)

    
llist = LinkedList()
node1 = Node2('a')
llist.head = node1
node2 = Node2('b')
node3 = Node2('c')
node4 = Node2('d')
node1.next = node2
node2.next = node3
node3.next = node4
print(llist)


# Another Implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    # Inserting element in a singly linked list
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
                
sll = SLinkedList()
sll.insert(1, 1)
sll.insert(2, 1)
sll.insert(3, 1)
sll.insert(4, 1)

sll.insert(0, 0)
sll.insert(5, 3)
sll.insert(6, -1)
sll.insert(7, -1)
print([node.value for node in sll])


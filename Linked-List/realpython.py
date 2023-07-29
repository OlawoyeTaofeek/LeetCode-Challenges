# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
    
# class Slinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
        
    
#     # traversing a list : Using Inbuilt Function:   
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
            
# sll1 = Slinkedlist()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# sll1.head = node1
# node1.next = node2
# node2.next = node3

# for node in sll1:
#     print(node.value)
# print([node.value for node in sll1])
        

# # Insertion : At the begining of a node  head -> Node -> Tail

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
#     def __repr__(self):
#         return self.value
    
# class Slinkedlist:
#     def __init__(self):
#         self.head = None
                
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.value)
#             node = node.next
#         return " -> ".join(nodes)

    
#     # Insertion at the beginning of a LinkedList
#     def add_first(self, node):
#         node.next = self.head
#         self.head = node
        
#     # Insertion at the end of a LinkedList
#     def add_to_last(self, node):
#         if self.head is None:
#             self.head = node
#             return 
#         for current_node in self:
#             pass
#         current_node.next = node

#     # traversing a list : Using Inbuilt Function:   
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
            
#     # Traversing a list method:
#     def traverse(self):
#         if self.head is None:
#             print('Linked list is empty')
#         else:
#             node = self.head
#             while node is not None:
#                 print(node.value)
#                 node = node.next
            
# sll2 = Slinkedlist()
# node1 = Node('a')
# node2 = Node('b')
# node3 = Node('c')
# node4 = Node('d')
# sll2.head = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4

# sll2.add_to_last(Node('e'))
# sll2.add_to_last(Node('f'))
# print(sll2)
# # print([node.value for node in sll2])
# # for node in sll2:
# #     print(node)
    
# print(sll2.traverse())
# print([node.value for node in sll2])

    
class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # traversing a list    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.ref
            
   #traversing a linked list
    def printLinkedList(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value, "-->", end =' ')
                node = node.next
            
    def insert(self, value, location):
        node = self.head
        if node is None:
            print('Linked List is empty')
        else:
            if location == 0:
                newNode = Node(value)
                newNode.ref = self.head
                self.head = newNode
            
            elif location == -1:
                newNode = Node(value)
                while node.ref is not None:
                    node = node.ref
                node.ref = newNode
            # or 
            # elif location == -1:
            #     newNode = Node(value)
            #     newNode.ref = None
            #     self.tail.ref = newNode
            #     self.tail = newNode
            
            else:
                i = 0
                newNode = Node(value)
                while i < location - 1:
                    node = node.ref
                    i += 1
                newNode.ref = node.ref
                node.ref = newNode
                
                
            
    # Adding an element to linked list(Last)                 
    def add_to_llist(self, value):
        newNode = Node(value)
        node = self.head
        if node is None:
            self.head = newNode
            return 
        # Add to tail
        while True:
            if node.ref is None:
                node.ref = newNode
                break
            node = node.ref
                    
    
    
                    
            
    
    
    
    
    
llist = SinglyLinkedList()
llist.printLinkedList()
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')

llist.head = node1
node1.ref = node2 
node2.ref = node3
node3.ref = node4

llist.add_to_llist('E')
llist.insert('G', -1)
llist.insert('F', 5)

current_node = node1
while True:
    print(current_node.value, '-->', end = " " )
    if current_node.ref is None:
        print(None)
        break
    current_node = current_node.ref
    
    
    
        
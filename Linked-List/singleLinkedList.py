# Create a node at a random point in the memory
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    #traversing a linked list
    def traverse(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value, "-->", end =' ')
                node = node.next
                
    # traversing a Linked list method 2
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    # Search for an element
    def search(self, x):
        node = self.head
        if node is None:
            print('The node is not present')
        i = 0
        while node is not None:
            if node.value == x:
                print(f'{x} exist in the linked list and at index {i}')
                return x
            node = node.next
            i += 1
        return f"{x} not an element in the linked list"
    
    # Finding the Index of an element in the linked list
    def LocateIndex(self, x):
        node = self.head
        if node is None:
            print('The node is not present')
        i = 0
        while node is not None:
            if node.value == x:
                print(f"{x} is located at index {i} ")
            node = node.next
            i += 1
            
                
    # Inserting element at the beginning
    def add_to_first(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    # Insert an element anywhere but not beginning or last
    # Adding element after a Given Node
    def add_after(self, value, x):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            newNode = Node(value)
            if node.value == x:
                newNode.next = node.next
                node.next = newNode
                return
        raise Exception(f"Node with data {x} not found")
        
    def add_to_middle1(self, value, x):
        node = self.head
        while node is not None:
            if node.value == x:
                break
            node = node.next
            
        if node is None:
            print('The node is not present')
        else:
            newNode = Node(value)
            newNode.next = node.next
            node.next = newNode
            
    def add_to_middle2(self, value, x):
        node = self.head
        # At the beginning
        if self.head is None:
            print('Linked list is empty')
            return
        if node.next == x:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            return 
        # Before the rest of the node
        while node.next is not None:
            if node.next.value == x:
                break
            node = node.next
        if node.next is None:
            print('The node is not present')
        else:
            newNode = Node(value)
            # nextNode = node.next
            # node.next = newNode
            # newNode.next = nextNode
            
            # OR
            newNode.next = node.next
            node.next = newNode
                     
    # Insert element at the end 
    def add_to_last(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return 
        for current_node in self:
            pass
        current_node.next = newNode
    
    # Insert element at the end method 2
    def add_to_end(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode   
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = newNode
                
    # Inserting an element into a linked list anywhere       
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
                node = self.head
                while node.next is not None:
                    node = node.next
                node.next = newNode           
                
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1   
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    # Delete 
    def delete(self, location):
        node = self.head
        if self.head is None:
            print('The linked list is empty')
        else:
            if location == 0:
                self.head = node.next
                    
            elif location == -1:
                while node.next.next is not None:
                    node = node.next
                node.next = None
            
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                nextNode = node.next
                node.next = nextNode.next
                
                
            # else:
            #     pass
                
    # Deleting first element      
    def delete_first(self):
        node = self.head
        if self.head is None:
            print('The linked list is empty')
        else:
            self.head = node.next
    
    # Deleting last element      
    def delete_last(self):
        node = self.head
        if self.head is None:
            print('The linked list is empty')
        else:
            while node.next.next is not None:
                node = node.next
            node.next = None
            
    # Deleting any element  
    
    
    
                
                    
             
    # Reversing a singly linked list
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
                    
                
sll = SinglyLinkedList()
sll.add_to_first(1)
sll.add_to_first(-1)
sll.add_to_last(2)
print(sll.add_to_end(3))
sll.insert(4, -1)
sll.insert(-2, 0)
sll.insert(3.5, 3)
sll.insert(5, -1)
# sll.add_to_middle1(2.5, 1)
# sll.add_to_middle2(1.5, 2.5)
# sll.add_after(4.5, 4)
print([node.value for node in sll])
# sll.delete(0)
# sll.delete_last()
sll.delete(-1)
# sll.delete_first()
# print([node.value for node in sll])
# print(sll.search(2.5))
# print(sll.search(10))
# print(sll.LocateIndex(2.5))
# print(sll.delete(3))
# # print(sll.reverse())
print(sll.traverse())


def remove(head, index):
    if index == 0:
        return head.next
    prev = None
    current = head
    count = 0
    
    while (current is not None) & (count < index):
        prev = current
        current = current.next
        count += 1
    if current is not None:
        prev.next = current.next
        
    return head
         
# print(linkedlistvalues(remove(head, 3)))

def insert(head, value, location):
    new_node = Node(value)
    if location == 0:
        new_node.next = head
        return new_node
    
    prev = None
    current = head
    count = 0
    
    while current and count < location - 1:
        prev = current 
        current = current.next
        count += 1
        
    if current:
        prev.next = new_node
        new_node.next = current
    else:
        prev.next = new_node
        new_node.next = None
        
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(5)

def linkedlistvalues(head):
    current = head 
    arr = []
    while current is not None:
        arr.append(current.value)
        current = current.next
    return arr

print(linkedlistvalues(head))

print(linkedlistvalues(insert(head, value=3, location=3)))
print(linkedlistvalues(insert(head, value=6, location=6)))
print(linkedlistvalues(insert(head, value=7, location=7)))
        
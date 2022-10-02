class Node:
    def __init__(self):
        self.val = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.next = None


    def get(self, index: int) -> int:
        node = self
        counter = 0
        while (node):
            if (counter == index):
                if (counter == 0):
                    return -1 if node.head == None else node.head
                else:
                    return node.val
            else:
                counter += 1
                node = node.next
                
        return -1  

    def addAtHead(self, val: int) -> None:
        if(self.head or self.head == 0):
            self.addAtIndex(1, self.head)
            self.head = val
            return
        else:
            self.head = val
        

    def addAtTail(self, val: int) -> None:
        node = self
        if(node.head == None):
            self.addAtHead(val)
            return
        while(node):
            if (node.next == None):
                node.next = Node()
                node.next.val = val
                return
                
            else:
                node = node.next
                continue
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node()
        newNode.val = val
        prev = self
        node = self
        counter = 0
        while (node):
            if (counter == index):
                if (counter == 0):
                    self.addAtHead(val)
                    return
                else:
                    newNode.next = node
                    prev.next = newNode
                    return
            else:
                if (counter == 0):
                    node = node.next
                else:
                    node = node.next
                    prev = prev.next
                counter += 1
        if (counter == index and counter == 1):
            self.next = newNode
            return
        if (counter == index):
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        prev = self
        node = self
        counter = 0
        while (node):
            if (counter == index):
                if (counter == 0):
                    if (node.next and node.next.next):
                        prev.head = node.next.val
                        prev.next = node.next.next
                        return
                    elif(node.next):
                        prev.head = node.next.val
                        prev.next = None
                        return
                    else:
                        prev.head = None
                        prev.next = None
                        return
            else:
                if (counter == 0):
                    node = node.next
                else:
                    node = node.next
                    prev = prev.next
                counter += 1



#code to loop over the linkedlist and print items
# node = obj
# while (node):
#     if(node == obj):
#         print(node.head)
#         node =node.next
#         continue
#     else:
#         print(node.val)
#         node = node.next


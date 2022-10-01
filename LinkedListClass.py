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
                    return node.head
                else:
                    return node.val
            else:
                counter += 1
                node = node.next
                
        return -1  

    def addAtHead(self, val: int) -> None:
        self.head = val
        

    def addAtTail(self, val: int) -> None:
        node = self
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
        # Next = None
        node = self
        counter = 0
        while (node):
            if (counter == index):
                if (counter == 0):
                    newNode.next = node
                    prev.head = newNode
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

    def deleteAtIndex(self, index: int) -> None:
        prev = self
        node = self
        counter = 0
        while (node):
            if (counter == index):
                if (counter == 0):
                    prev.head = node.next
                    return
                else:
                    prev.next = node.next
                    return
            else:
                if (counter == 0):
                    node = node.next
                else:
                    node = node.next
                    prev = prev.next
                counter += 1
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3,0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
obj.get(4)
print(obj.get(4))


node = obj
while (node):
    if(node == obj):
        print(node.head)
        node =node.next
        continue
    else:
        print(node.val)
        node = node.next

# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtTail(34)
# obj.addAtTail(32)

# obj.addAtIndex(1,2) #problem with addAtIndex and deleteAtIndex methods
# node = obj
# while (node):
#     if(node == obj):
#         print(node.head)
#         node =node.next
#         continue
#     else:
#         print(node.val)
#         node = node.next
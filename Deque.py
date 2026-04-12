#Deque

class deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if (self.isEmpty()):
            print("Deque is Empty")
        else:
            return self.items.pop(0)
        
    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtEnd(self):
        return self.items.pop()

dq = deque()
dq.insertAtEnd(5)
dq.insertAtEnd(55)
dq.insertAtFront(10)
dq.insertAtFront(100)
print(dq.deleteAtFront())
print(dq.deleteAtEnd())

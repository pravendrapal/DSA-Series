class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None
        
class DoublyLL:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return

        t = self.head
        while(t.next != None):
            t = t.next
        t.next = temp
        temp.prev = t

    def InsertAtBeg(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp

        temp.next = self.head
        self.head = temp
        
    def InsertAtMid(self,value,x):
        temp = Node(value)
        t = self.head
        while(t.next != None):
            if(t.data == x):
                temp.next = t.next
                t.next.prev = temp
                t.next = temp
                temp.prev = t
            t = t.next

    def DeleteDLL(self,value):
        if (self.head == None):
            print("Linked List is Empty")
            return
        
        t = self.head
        if (t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next

        t.prev.next = None

        


    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data, end=" <--> ")
            t = t.next
        print(t.data)

obj = DoublyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.InsertAtEnd(50)
obj.InsertAtBeg(5)
obj.InsertAtBeg(2)
obj.InsertAtMid(15,10)
obj.InsertAtMid(25,20)
obj.InsertAtMid(27,25)
obj.InsertAtMid(35,30)
obj.InsertAtMid(45,40)
obj.DeleteDLL(2)
obj.DeleteDLL(40)
obj.DeleteDLL(50)
obj.printDLL()

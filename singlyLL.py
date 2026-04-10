class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:
    def __init__(self,head=None):
        self.head = head

    def InsertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next 
            t1.next = temp
        else:
            self.head = temp

    def InsertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def InsertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
    def DeleteLL(self,value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        while (t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None
    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)
    
obj = SinglyLL()
obj.InsertAtEnd(10)
obj.InsertAtEnd(20)
obj.InsertAtEnd(30)
obj.InsertAtEnd(40)
obj.InsertAtBeg(5)
obj.InsertAtMid(25,20)
obj.InsertAtMid(35,30)
obj.DeleteLL(40)
obj.DeleteLL(10)
obj.printLL()
pravendra 
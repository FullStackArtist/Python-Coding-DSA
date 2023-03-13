class Node():
    def __init__(self,val):
        self.data=val
        self.nextad=None
class LinkedList():
    def __init__(self):
        self.headval=None

# Travelling through our Linked list """

    def printval(self,ls):
        print(" Linked list is as shown")
        head=ls.headval
        while head is not None:
            print(head.data)
            head=head.nextad
        return

# Creating Linked List  """
    def create(self,n):
        ls=LinkedList()
        print(ls)
        data=input(" Value ")
        rf=Node(data)
        ls.headval=rf
        for i in range(1,n):
            data=input(" Value ")
            nf=Node(data)
            rf.nextad=nf
            rf=nf
        return ls

    def delete(self,data,ls):
        head=ls.headval
        if head.data== data:
            ls.headval=ls.headval.nextad
            return
        prev=ls.headval
        head=head.nextad
        while head is not None:
            if head.data==data:
                prev.nextad=head.nextad
                return
            prev=head
            head=head.nextad
        
            
            
        return " Value not found "

    def insert(self,data,ls):
        head=ls.headval
        while head is not None:
            if head.nextad is None:
                head.nextad=Node(data)
                return
            head=head.nextad
        
n=int(input(" number of nodes for linked list "))
ls=LinkedList().create(n) # object on the fly
print()
LinkedList().printval(ls) # object on the fly
dt=input(" Enter value to be deleted from list ")
LinkedList().delete(dt,ls)
#LinkedList().printval(ls)
#dt=input(" Enter value to be insegrted at end ")
#LinkedList().insert(dt,ls)
LinkedList().printval(ls)





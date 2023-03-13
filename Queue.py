class Node():
    def __init__(self,data):
        self.data=data
        self.nextval=None
class Queue():
    def __init__(self):
        self.headval=None

    def createqueue(self,qs,n):
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

    def deletequeue(self,qs):
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

    def insertqueue(self,qs,data):
        head=ls.headval
        while head is not None:
            if head.nextad is None:
                head.nextad=Node(data)
                return
            head=head.nextad

    
    def printval(self,ls):
        print(" Linked list is as shown")
        head=ls.headval
        while head is not None:
            print(head.data)
            head=head.nextad
        return

qs=Queue()
print(qs)
n=int(input())
qs=Queue().createqueue(qs,n)

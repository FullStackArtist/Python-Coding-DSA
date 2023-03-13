class Node():
    def __init__(self,val):
        self.data=val
        self.nextad=None
class StackList():
    def __init__(self):
        self.headval=None

# Travelling through our Stack list """

    def printval(self,ls):
        print(" Stack value is as shown :- ")
        head=ls.headval
        while head is not None:
            print(head.data)
            head=head.nextad
        return

# Creating Stack
    def create(self,n):
        ls=StackList()
        print(ls)
        data=input(" Value ")
        rf=Node(data)
        ls.headval=rf
        for i in range(1,n):
            data=input(" Value ")
            nf=Node(data)
            nf.nextad=ls.headval
            ls.headval=nf
        return ls

    def push(self,ls,data):
        nf=Node(data)
        nf.nextad=ls.headval
        ls.headval=nf

    def pop(self,ls):
        #head=ls.headval
        data=ls.headval.data
        #head=ls.headval.nextad
        ls.headval=ls.headval.nextad
        print(data)
        print("removed from stack")
        return ls


    def stackpop(self,ls):

        return ls.headval.data


n=int(input(" number of nodes for stack:-  "))
ls=StackList().create(n) # object on the fly
print()
StackList().printval(ls) # object on the fly
ls=StackList().pop(ls)
print()
StackList().printval(ls)
data=input("value to be inserted:- ")
StackList().push(ls,data)
print()
StackList().printval(ls)
print()
print("stackpop at same time value is:- ")
print(StackList().stackpop(ls))






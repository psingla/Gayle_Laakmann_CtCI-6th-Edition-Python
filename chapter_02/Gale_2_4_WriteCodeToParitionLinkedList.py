class sll:
    data=None
    next=None
    
    def __init__(self,p_data):
        self.data=p_data
    
    def addNodeAtEnd(self,p_data):
        newNode=sll(p_data)
        self.next=newNode
        return(newNode)

parition=5
head=sll(3)
current=head
current=current.addNodeAtEnd(5)
current=current.addNodeAtEnd(8)
current=current.addNodeAtEnd(5)
current=current.addNodeAtEnd(10)
current=current.addNodeAtEnd(2)
current=current.addNodeAtEnd(1)

"""
current=head
while (current!=None):
    print(current.data)
    current=current.next
"""

frontNode=sll(-pow(10,6)) #none is not working here. Need to check why
frontNode.next=head
current=head
while (current.next!=None):
   
    #print(current.data,current.next.data)
    currentsNextNode=current.next
    if (currentsNextNode.data<parition):
        if(currentsNextNode.next!=None):
            current.next=currentsNextNode.next
        else:
            current.next=None
        frontNode.next=currentsNextNode
        currentsNextNode.next=head
        head=currentsNextNode
    else:
        current=current.next
    
    
current=head
while (current!=None):
    print(current.data)
    current=current.next   
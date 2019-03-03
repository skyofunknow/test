#单链表的基本操作
#链表的结点
class Node():
    def __init__(self,data,p=0):
        self.data=data
        self.next=p

class LinkedList():
    def __init__(self):
        self.head=Node(0) #哨兵结点          
        
    def showNodes(self):
        p=self.head.next
        while(p!=0):
            print(p.data)
            p=p.next
            
    def add(self,data): #队尾增加结点
        p=self.head
        while(p.next!=0):
            p=p.next
        newnode=Node(data)
        p.next=newnode
    
    def addList(self,dataList):
        for data in dataList:
            self.add(data)
    
    def reserve(self):   #反转单链表   
        
        if(self.head.next==0):  #单链表中无数据结点
            return
        tail=self.head.next #反转后的尾结点
        self.head.next=0  #哨兵结点 不指向链表
        p=tail
        q=p.next
        while(q!=0):             
            h=q.next
            q.next=p
            p=q
            q=h
            
        tail.next=0
        self.head.next=p
    
    def midNode(self): #求链表的中间结点，一个指针一次走一步，一个指针一次走两步
        if(self.head.next==0):  #单链表中无数据结点
            print("None")
            return
        h1=self.head.next
        h2=self.head.next
        while(h2.next!=0 and h2.next.next!=0):
            h1=h1.next
            h2=h2.next.next
        print(h1.data)
    
    def delTailn(self,n): #删除链表中倒数第n个结点
        if(n<1):
            print("n must greater than 0")
            return
        p=self.head.next
        i=0
        while(p!=0 and i<n-1):
            i=i+1
            p=p.next
        if(i<n-1):
            print("Num of LinkedList  is less than n")
            return
        h=self.head
        while(p.next!=0):
            h=h.next
            p=p.next
        q=h.next
        h.next=q.next
        q.next=0
        
    def isLinkedListhasCircle(self): #检测链表中是否存在环
        
        h1=self.head.next
        h2=self.head.next
        while(h2.next!=0 and h2.next.next!=0):
            h1=h1.next        #走一步
            h2=h2.next.next   #走两步
            if(h1==h2):
                return True
        return False

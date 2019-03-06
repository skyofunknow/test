class Queue():
    def __init__(self,n):
        self.length=n #队列大小
        self.items=n*[0]
        self.head=0  #队头出队
        self.tail=0  #队尾入队
    def enqueue(self,data):#入队列
        if(self.head==0 and self.tail==self.length): #队列已满
            print("Full")
            return
        elif self.tail==self.length:
            self.items[0:self.tail-self.head]=self.items[self.head:self.tail]            
            self.tail=self.tail-self.head
            self.head=0
        self.items[self.tail]=data
        self.tail+=1
    def dequeue(self):#出队列
        if self.head==self.tail:
            print("Empty!")
            return
        else:
            item = self.items[self.head]
            self.head+=1
            return item

#循环队列
class CircularQueue():
    def __init__(self,n):
        self.length=n #队列大小
        self.items=n*[0]
        self.head=0
        self.tail=0
    def enqueue(self,data):#浪费数组一个存储空间
        if (self.tail+1)%self.length==self.head:#
            print("Full")
            return
        self.items[self.tail]=data
        self.tail=(self.tail+1)%self.length
    def dequeue(self):
        if self.head==self.tail:
            print("Empty!")
            return
        else:
            item = self.items[self.head]
            self.head=(self.head+1)%self.length
            return item

#CAS指令执行时，当且仅当内存地址V存储的值与预期值A相等时，将内存地址V存储的值修改为B，
#否则就什么都不做。整个比较并替换的操作是一个原子操作
    

import random
MAX_LEVEL=4

#实现了基于链表的“二分查找”
#返回随机层数
def randomLevel():
    k=1
    while random.randint(1,100)%2:
        k+=1
    k=k if k<MAX_LEVEL else MAX_LEVEL
    return k

#跳表遍历
def traversal(skiplist):
    level=skiplist.level
    i=level-1
    while i>=0:
        level_str="header"
        header=skiplist.header
        while header:
            level_str+="->%s"%header.key
            header=header.forward[i]
        print(level_str)
        i-=1

class Node():
    def __init__(self,level,key,value):
        self.key=key
        self.value=value
        self.forward=[None]*level
        
class Skiplist():
    def __init__(self):
        self.level=0
        self.header=Node(MAX_LEVEL,0,0)
        
    def insert(self,key,value):
        updata=[None]*MAX_LEVEL
        p=self.header
        q=None
        k=self.level
        i=k-1
        #updata为待更新结点的前一个结点
        while i>=0:
            q=p.forward[i]
            while q and q.key<key:
                p=q
                q=q.forward[i]
            updata[i]=p
            i-=1
        if q and q.key==key:
            return False
        
        k=randomLevel()
        if k>self.level:
            i=self.level
            while i<k:
                updata[i]=self.header
                i+=1
            self.level=k
        q=Node(k,key,value)
        i=0
        while i<k:
            q.forward[i]=updata[i].forward[i]
            updata[i].forward[i]=q
            i+=1
        return True
    
       
    def delete(self,key):
        updata=[None]*MAX_LEVEL
        p=self.header
        q=None
        k=self.level
        i=k-1
        #updata为待查找结点的前一个结点
        while i>=0:
            q=p.forward[i]
            while q and q.key<key:
                p=q
                q=q.forward[i]
            updata[i]=p
            i-=1
        if q and q.key==key:
            i=0        
            while i<self.level:
                if updata[i].forward[i]==q:
                    updata[i].forward[i]=q.forward[i]
                i+=1
            del q
            i=self.level-1
            while i>=0:
                if not self.header.forward[i]:
                    self.level-=1
                i-=1
                return True
        else:
            return False
        
    def search(self,key):        
        i=self.level-1
        #返回最高层数
        while i>=0:
            q=self.header.forward[i]
            while q and q.key<=key:                
                if q.key==key:
                    return q.key,q.value,i
                q=q.forward[i]            
            i-=1
        return None
    
def main():
    number_list=(7,4,1,8,5,2,9,6,3)
    skiplist=Skiplist()
    for number in number_list:
        skiplist.insert(number,None)
    traversal(skiplist)
    print( skiplist.search(4) )
    skiplist.delete(4)
    traversal(skiplist)
        
        
            
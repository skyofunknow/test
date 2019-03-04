#栈
class Stack():
    def __init__(self):
        self.__items=[]#两个下划线，类的私有成员
    
    def size(self):
        return len(self.items)
    
    #栈顶元素
    def peek(self):
        if self.size()==0:
            print("None")
        else:
            return self.items[self.size()-1]
    
    def push(self,data):#压栈
        self.items.append(data)
        
    def pop(self):#出栈
        if self.size()==0:
            print("None")
        else:
            return self.items.pop()
        

#节点的高度＝节点到叶子节点的最长路径（边数）
#节点的深度＝根结点到这个节点所经历的边的个数
#节点的层数＝节点的深度＋1
#数的高度＝根节点的高度

class Node():
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

#前序遍历
def preOrder(root):
    if root == None:
        return
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)
    
#中序遍历
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value)    
    inOrder(root.right)

#后序遍历
def postOrder(root):
    if root == None:
        return
    postOrder(root.left)       
    postOrder(root.right)
    print(root.value)
    
    
#已知前序和中序遍历，求后序遍历    
def findTree(preList,midList,afterList):
    if len(preList)==0:
        return
    if len(preList)==1:
        afterList.append(preList[0])
        return
    root=preList[0]
    n=midList.index(root)
    #将前序和中序分为两部分,分别递归调用
    findTree(preList[1:n+1],midList[:n],afterList)
    findTree(preList[n+1:],midList[n+1:],afterList)
    afterList.append(root)
    
    
if __name__=="__main__":
    root=Node("D",Node("B",Node("A"),Node("C")),Node("E",right=Node("G",Node("F"))))
    #      D
    #     / \
    #    B   E
    #   / \   \
    #  A   C   G
    #         /
    #        F 
    preOrder(root)
    print("\n")
    inOrder(root)
    print("\n")
    postOrder(root)
    preList=list("12473568")
    midList=list("47215386")
    afterList=list()
    findTree(preList,midList,afterList)
    
    
    
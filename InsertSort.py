#插入排序 从后往前在有序区间查找
def InsertSort(a):
    l=len(a)
    for i in range(1,l):
        value=a[i]
        for j in range(i-1,-1,-1):
            if(value<a[j]):#数据移动
                a[j+1]=a[j]
            else:
                a[j+1]=value#插入数据
                break

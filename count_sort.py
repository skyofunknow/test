#计数排序
def count_sort(a):
    max_value=max(a)
    n=len(a)
    c=(max_value+1)*[0]
    #每个元素的个数
    for i in range(n):
        c[a[i]]+=1
    #c[k]:小于等于k的元素个数
    for i in range(1,max_value+1):
        c[i]=c[i]+c[i-1]
    r=n*[0]
    for i in range(n):
	#a[i]放在满足条件的最后一个位置
        index=c[a[i]]-1
        r[index]=a[i]
        c[a[i]]-=1
    a[:]=r[:]
    
    
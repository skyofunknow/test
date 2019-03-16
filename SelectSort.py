#选择排序 
#不稳定排序
#从小到大排序
def SelectSort(a):
    l=len(a)
    for i in range(l-1):
        min_index=i        
        for j in range(i+1,l):
            if(a[min_index]>a[j]):
                min_index=j           
            a[i],a[min_index]=a[min_index],a[i]            

#双向选择排序
def BiSelectSort(a):
    l=len(a)
    for i in range(l//2):
        min=i
        max=l-i
        min_index=i
        max_index=l-i-1
        for j in range(min,max):#先更新，再缩放
            if(a[min_index]>a[j]):
                min_index=j
            if(a[max_index]<a[j]):
                max_index=j
            a[i],a[min_index]=a[min_index],a[i]
            a[l-i-1],a[max_index]=a[max_index],a[l-i-1]

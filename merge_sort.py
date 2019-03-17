#归并排序
def merge_sort(a):
    n=len(a)
    merge_sort_c(a,0,n-1)
    
def merge_sort_c(a,p,r):
    if p>=r: #递推终止
        return
    q=int((p+r)/2)
    merge_sort_c(a,p,q)
    merge_sort_c(a,q+1,r)
    merge(a,p,q,r)#将两个有序的数组合并为一个

def merge(a,p,q,r):    
    i=p
    j=q+1
    k=0
    b=(r-p+1)*[0]#申请一个大小和a[p...r]一样的临时数组
    while i<=q and j<=r:
        if a[i]<=a[j]:
            b[k]=a[i]
            k+=1
            i+=1
        else:
            b[k]=a[j]
            k+=1
            j+=1
    while i<=q:
        b[k]=a[i]
        k+=1
        i+=1
    while j<=r:
        b[k]=a[j]
        k+=1
        j+=1
    a[p:r+1]=b[:]
            
        
        
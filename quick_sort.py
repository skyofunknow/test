#快排
def quick_sort(a):    
    n=len(a)
    quick_sort_c(a,0,n-1)

def quick_sort_c(a,l,r):
    if l>=r:
        return
    pos=partition(a,l,r)
    quick_sort_c(a,l,pos-1)
    quick_sort_c(a,pos+1,r)

def partition(a,l,r):    
    pivot=a[r]
    i=l
    j=l
    while j<r:
        if a[j]<pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
        j+=1
    a[i],a[r]=a[r],a[i]
    return i

#求无序数组的第K大元素  O(n)
def topNItem(a,K):
    n=len(a)
    if n<K:
        print("None")
        return
    l=0
    r=n-1
    while(l<r):
       pos=partition(a,l,r)
       if pos==K-1:
           return a[pos]
       if pos>K-1:
           r=pos-1
       if pos<K-1:
           l=pos+1
       
    
    
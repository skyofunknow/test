
def bsearch(a,value):
    n=len(a)
    low=0
    high=n-1
    while(low<=high):
        mid = low+((high-low)>>1)
        if value==a[mid]:
            return mid
        elif a[mid]<value:
            low=mid+1
        else:
            high=mid-1
    return -1

#查找一个值等于给定值的元素
def bsearch1(a,value):
    n=len(a)
    low=0
    high=n-1
    while(low<=high):
        mid = low+((high-low)>>1)
        if a[mid]>value:
            high=mid-1
        elif a[mid]<value:
            low=mid+1
        elif mid==0 or a[mid-1]!=value:
            return mid        
        else:
            high=mid-1
    return -1

#查找最后一个值等于给定值的元素
def bsearch2(a,value):
    n=len(a)
    low=0
    high=n-1
    while(low<=high):
        mid = low+((high-low)>>1)
        if a[mid]>value:
            high=mid-1
        elif a[mid]<value:
            low=mid+1
        elif mid==n-1 or a[mid+1]!=value:
            return mid        
        else:
            low=mid+1
    return -1

#查找第一个大于等于给定值的元素
def bsearch3(a,value):
    n=len(a)
    low=0
    high=n-1
    while(low<=high):
        mid = low+((high-low)>>1)        
        if a[mid]<value:
            low=mid+1
        elif mid==0 or a[mid－1]<value:
            return mid        
        else:
            high=mid-1
    return -1

#查找最后一个小于等于给定值的元素
def bsearch4(a,value):
    n=len(a)
    low=0
    high=n-1
    while(low<=high):
        mid = low+((high-low)>>1)        
        if a[mid]>value:
            high=mid-1
        elif mid==n-1 or a[mid+1]>value:
            return mid        
        else:
            high=mid+1
    return -1
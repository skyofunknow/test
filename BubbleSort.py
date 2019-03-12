#冒泡排序
#稳定排序
def BubbleSort(a):
    n=len(a)
    for i in range(n):
        flag=0     #提前退出冒泡循化的flag
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=1
        if flag==0:
            break

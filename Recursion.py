#递归需满足的三个条件
#1 一个问题的解可以分解为几个子问题的解
#2 这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
#3 存在递归终止条件
#写递归代码的关键是找到将大问题分解为小问题的规律，并基于此写出递推公式，然后再推敲终止条件
#最后将递推公式和终止条件翻译成代码

#n个台阶，每次可以走1次或2次，共多少种走法
hasSolvedList={}
def f(n): 
    if n==1:
        return 1
    if n==2:
        return 2
    if n in hasSolvedList.keys():#避免重复计算
        return hasSolvedList[n]
    else:
        ret = f(n-1)+f(n-2)
        hasSolvedList[n]=ret
        return ret
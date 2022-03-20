'''
问题描述
Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。
'''
n = int(input())
a = [1 for i in range(n)]
for i in range(2, n):
    a[i]=(a[i-1]+a[i-2])%10007
print(a[n-1])
'''
问题描述
给出n个数，找出这n个数的最大值，最小值，和。
输入格式
第一行为整数n，表示数的个数。
第二行有n个数，为给定的n个数，每个数的绝对值都小于10000。

输出格式
输出三行，每行一个整数。第一行表示这些数中的最大值，第二行表示这些数中的最小值，第三行
'''
if __name__ == '__main__':
    n = int(input())
    lst = list(map(int,input().split()))
    if len(lst)==n:
        ma = max(lst)
        mi = min(lst)
        s = sum(lst)
    print(ma)
    print(mi)
    print(s)

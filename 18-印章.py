'''
问题描述
　　共有n种图案的印章，每种图案的出现概率相同。小A买了m张印章，求小A集齐n种印章的概率。
输入格式
　　一行两个正整数n和m
输出格式
　　一个实数P表示答案，保留4位小数。
'''
# import numpy as np
n, m = map(int, input().split())
# dp = [[0]*25]*25
dp = [[0 for _ in range(25)] for _ in range(25)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if i < j:
            dp[i][j] = 0
        elif j == 1:
            dp[i][j] = (1 / n) ** (i - 1)
        else:
            dp[i][j] = (dp[i - 1][j]) * j / n + (dp[i - 1][j - 1]) * ((n - j + 1) / n)  # 状态转移函数

s = float(dp[m][n])
print("%.4f" % s)  # 按照题目要求输出四位小数
# print('{:.4f}'.format(dp[m][n]))


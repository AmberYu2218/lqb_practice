'''
问题描述
　　有一个N x N的方格,每一个格子都有一些金币,只要站在格子里就能拿到里面的金币。你站在最左上角的格子里,每次可以从一个格子走到它右边或下边的格子里。请问如何走才能拿到最多的金币。
输入格式
　　第一行输入一个正整数n。
　　以下n行描述该方格。金币数保证是不超过1000的正整数。
输出格式
　　最多能拿金币数量。
'''
n = int(input())
# 输入数组方式1
a = [list(map(int, input().split())) for j in range(n)]
# 输入数组方式2
# for i in range(n):
#     nums.append(list(map(int, input().split())))

# 第一列与第一行元素只能从同列的上一个或同行的前一个取得
for i in range(1, n):
    a[0][i] += a[0][i - 1]
    a[i][0] += a[i - 1][0]

# 计算每一个元素从上一步到这一步的最大值
for i in range(1, n):
    for j in range(1, n):
        a[i][j] += max(a[i - 1][j], a[i][j - 1])
print(a[-1][-1])

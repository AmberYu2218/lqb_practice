'''
问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
下面给出了杨辉三角形的前4行：
   1
  1 1
 1 2 1
1 3 3 1
给出n，输出它的前n行。
输入格式：输入包含一个数n。
输出格式：输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
'''
n = int(input())
lst = [[0 for i in range(n)] for j in range(n)]  # 定义一个二维数组，初始化为0
for i in range(n):
    lst[i][0] = 1
    lst[i][i] = 1
for i in range(1, n):
    for j in range(1, i + 1):
        lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1]
for i in range(n):
    for j in range(i+1):
        print(lst[i][j], ' ', end='')
    print()
# list1 = []
# for n in range(n):
#     row = [1]  # 第一行第一列为1
#     list1.append(row)
#     if n == 0:
#         for num in row:  # 这里主要是为输出做的格式处理
#             print(num, end=" ")
#             print()
#         continue
#     for m in range(1, n):
#         row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#     row.append(1)
#     for num in row:
#         print(num, end=" ")
#     print()

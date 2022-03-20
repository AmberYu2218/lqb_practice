'''
问题描述
给定圆的半径r，求圆的面积。
输入格式
输入包含一个整数r，表示圆的半径。
输出格式
输出一行，包含一个实数，四舍五入保留小数点后7位，表示圆的面积。
'''
from math import pi
r = int(input())
print('{0:.7f}'.format(pi*r*r))

# print('%.7s' % pi*r*r)
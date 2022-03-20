'''
Python map() 函数：
    作用：map() 会根据提供的函数对指定序列做映射。以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
    语法：map(function, iterable, ...)
    参数：function -- 函数；iterable -- 一个或多个序列
    返回值：Python 3.x 返回迭代器。

split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
'''
def add(m,n):
    return m+n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m, n = map(int, input().split())
    print(add(m, n))


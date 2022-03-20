def fun(n):
    lst = []
    for i in range(len(n)):
        if i:
            for j in range(i - 1, -1, -1):
                if n[i] < n[j]:
                    lst.append(j)
                    break
                else:
                    if j == 0:
                        lst.append(-1)
        else:
            lst.append(-1)
    return lst

def fun1(n):
    lst = []
    # if !n or len(n)==0:


if __name__ == '__main__':
    print(fun([5, 3, 1, 6, 4]))
if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 200:
        lst = list(map(int, input().split()))
        lst.sort()
    if n == len(lst):
        for i in range(len(lst)):
            if abs(lst[i]) < 10000:
                print(lst[i], end=' ')
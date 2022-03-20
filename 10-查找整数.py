if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    a = int(input())
    for i in range(n):
        if lst[i] <= 10000:
            if a == lst[i]:
                print(i+1)
                break
            elif i == n-1:
                print(-1)
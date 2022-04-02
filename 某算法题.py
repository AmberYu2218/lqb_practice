'''
三个骰子能组成多少数
'''
for i in range(3):
    inp = list(map(int, input().split()))
ans = 0
for a in range(6):
    for b in range(6):
        for c in range(6):
            ans+=1
for a in range(6):
    for c in range(6):
        for b in range(6):
            ans+=1
for b in range(6):
    for a in range(6):
        for c in range(6):
            ans+=1
for b in range(6):
    for c in range(6):
        for a in range(6):
            ans+=1
for c in range(6):
    for a in range(6):
        for b in range(6):
            ans+=1
for c in range(6):
    for b in range(6):
        for a in range(6):
            ans+=1
print(ans)
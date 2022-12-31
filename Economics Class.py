# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().strip().split()))
    d = list(map(int,input().strip().split()))
    r = 0
    for j in range(n):
        if s[j]==d[j]:
            r+=1
    print(r)
        

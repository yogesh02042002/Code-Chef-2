# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    p=x-y
    pro=x+((10/100)*x)
    res=pro-p
    print(round(res))

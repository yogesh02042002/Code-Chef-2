for _ in range(int(input())):
    x,y=map(int,input().split())
    a=500-2*x
    b=1000-4*(x+y)
    c=a+b
    d=1000-(y)*4
    r=500-2*(x+y)
    i=d+r
    if c>=i:
        print(c)
    else:
        print(i)

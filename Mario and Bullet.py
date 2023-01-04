# cook your dish here
for i in range(int(input())):
    x,y,z=map(int,input().split())
    p=z-(y//x)
    if p>0:
        print(p)
    else:
        print(0)

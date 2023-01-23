# cook your dish here
import math
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x=math.sqrt((x1**2)+(y1**2))
    y=math.sqrt((x2**2)+(y2**2))
    if x>y:
        print("Alex")
    elif x<y:
        print("Bob")
    else:
        print("Equal")

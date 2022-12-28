# cook your dish here
def digitsum(a):
    num=str(a)
    sum=0
    for i in num:
        sum=sum+int(i)
    return sum
    
for _ in range(int(input())):
    n=int(input())
    x=n+1
    while(1):
        if((digitsum(n)%2==0 and digitsum(x)%2!=0)or(digitsum(n)%2!=0 and digitsum(x)%2==0)):
            print(x)
            break
        x=x+1
    

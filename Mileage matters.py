# cook your dish here
for i in range(0,int(input())):
    n, x, y, a, b = map(int, input().split())
    petrol = n / a * x
    diesel = n / b * y
    if petrol == diesel:
        print("ANY")
    elif petrol < diesel:
        print("PETROL")
    else:
        print("DIESEL")

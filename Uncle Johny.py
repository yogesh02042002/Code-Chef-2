# cook your dish here
for i in range(int(input())): 
    N = int(input())
    A = list(map(int , input().split()))
    K = int(input())
    num = A[K-1]
    A.sort() 
    print(A.index(num)+1)

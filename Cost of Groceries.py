# cook your dish here
for i in range(int(input())):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  total_cost = 0
  for j in range(n):
    if a[j] >= x:
      total_cost += b[j]
  print(total_cost)

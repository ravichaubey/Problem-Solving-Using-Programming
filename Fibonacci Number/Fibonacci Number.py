n = int(input())

a = 0
b = 1

if n <= 1:
    print(n)
else:
    for i in range(2,n+1):
        c = a+b
        a,b = b,c
    print(c)
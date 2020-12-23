a,b = 0,1
c = a+b

n = int(input())

for i in range(2,n+1):
    c = (a+b)%10
    b,a = c,b

if n<=1:
    print(n)
else:
    print(c)
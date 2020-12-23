def pisanoPeriod(m):
	a=0
	b=1
	c= a+b
	for i in range(0,m*m):
		c= (a+b)%m
		a=b
		b=c
		if( a == 0 and b == 1):
			return (i+1)

def fibonacci(n):
    a,b = 0,1
    for _ in range(2,n+1):
        c = a+b
        a,b = b,c
    return c
	
n,m = map(int,input().split())
p = pisanoPeriod(m)
x = n%p

print(fibonacci(x)%m)
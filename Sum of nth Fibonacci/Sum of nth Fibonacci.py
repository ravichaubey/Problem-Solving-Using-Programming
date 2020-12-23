def getFibonacci(n):
    a,b = 0,1
    if n<= 1:
        return n
    else:
        for _ in range(2,n+1):
            c = a+b
            a,b = b,c
        return c

def sumOfFib(x):
    #x is F(2n+1)th term
    return x-1

if __name__ == "__main__":
    n = int(input())
    x = getFibonacci(n+2)
    print(sumOfFib(x)%10)

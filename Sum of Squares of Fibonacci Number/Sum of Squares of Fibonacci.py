def getFibonacci(n):
    a,b = 0,1
    c = a+b
    if n<= 0:
        return n
    else:
        for _ in range(2,n+1):
            c = a+b
            a,b = b,c
        return c

def sumOfSquares(n):
    return getFibonacci(n) * getFibonacci(n+1)

if __name__ == "__main__":
    n = int(input())
    print(sumOfSquares(n) % 10)
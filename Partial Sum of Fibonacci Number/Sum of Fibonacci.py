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
    
def getRem(m,n):
    res = getFibonacci(n+2) + 10 - getFibonacci(m+1)
    return res%10

if __name__ == "__main__":
    m,n = map(int,input().split())
    print(getRem(m,n))
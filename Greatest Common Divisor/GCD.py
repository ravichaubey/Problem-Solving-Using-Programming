# Euclidean GCD(a,b) == GCD(a`,b)

def gcd(a,b):
    if b == 0:
        return a
    else:
        aDash = a%b
        return gcd(b,aDash)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
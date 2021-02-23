def factorial(n):
    assert n >= 0 and int(n) == n, "Positive Integers Only"
    if n in [0,1]:
        return 1
    return n*factorial(n-1)

print(factorial(int(input("Enter n ==> "))))
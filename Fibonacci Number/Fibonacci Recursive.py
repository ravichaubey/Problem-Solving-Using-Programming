def f(n):
    assert n>=0 and int(n) == n, "Non Negative Integers Only"
    if n in [0,1]:
        return n
    return f(n-1) + f(n-2)

print(f(int(input("Enter Number ==> "))))
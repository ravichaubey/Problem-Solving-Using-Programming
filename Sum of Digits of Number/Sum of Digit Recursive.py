def sumOfDigits(n):
    assert n>=0 and n == int(n), "Positive Integers Only.."
    if n == 0:
        return 0
    else:
        print(int(n%10)," ",int(n/10))
        return int(n % 10) + sumOfDigits(int(n/10))

print(sumOfDigits(int(input())))
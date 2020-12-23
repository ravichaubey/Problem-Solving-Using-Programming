def maxProductTwo(arr):
    max1,max2 = float('-inf'),float('-inf')
    for i in arr:
        if i>max1:
            max2 = max1
            max1 = i
        elif i>max2:
            max2 = i
    return max1*max2
    
n = int(input())
arr = list(map(int,input().split()))
print(maxProductTwo(arr))
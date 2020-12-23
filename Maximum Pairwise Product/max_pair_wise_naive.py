arr = list(map(int,input().split()))

res = 0

n = len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[i] * arr[j] >res:
            res = arr[i] * arr[j]

print(arr,res)
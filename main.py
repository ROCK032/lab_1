arr = [5, 9, 7, 6, 15, 49, 88, 168, 1]

n = len(arr)
for i in range(n):
    minimum = i
    for j in range(i+1, n):
        if arr[j] < arr[minimum]:
            minimum = j
    arr[i], arr[minimum] = arr[minimum], arr[i]

print(arr)
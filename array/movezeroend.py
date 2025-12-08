n = int(input())
arr = list(map(int, input().split()))

index = 0

for x in arr:
    if x != 0:
        arr[index] = x
        index += 1

while index < n:
    arr[index] = 0
    index += 1

print(*arr)

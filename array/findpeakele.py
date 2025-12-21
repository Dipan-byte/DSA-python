n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if (i == 0 or arr[i] >= arr[i - 1]) and \
       (i == n - 1 or arr[i] >= arr[i + 1]):
        print("Peak Element:", arr[i])
        break

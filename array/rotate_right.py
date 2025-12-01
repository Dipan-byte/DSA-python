n = int(input().strip())

if n == 0:
    exit()

arr = list(map(int, input().split()))
k = int(input().strip())

k = k % n
if k < 0:
    k += n  # handle negative k if needed


def reverse(a, start, end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1


# Step 1: reverse whole array
reverse(arr, 0, n - 1)
# Step 2: reverse first k elements
reverse(arr, 0, k - 1)
# Step 3: reverse remaining elements
reverse(arr, k, n - 1)

print(" ".join(map(str, arr)))

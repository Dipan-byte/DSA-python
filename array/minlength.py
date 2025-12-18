n = int(input())
arr = list(map(int, input().split()))
S = int(input())

left = 0
current_sum = 0
min_len = float('inf')

for right in range(n):
    current_sum += arr[right]

    while current_sum >= S:
        min_len = min(min_len, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_len == float('inf'):
    print(0)
else:
    print("Minimum Length:", min_len)

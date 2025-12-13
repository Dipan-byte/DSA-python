n = int(input())
arr = list(map(int, input().split()))

s = set(arr)
longest = 0

for x in s:
    if x - 1 not in s:   # start of sequence
        current = x
        length = 1

        while current + 1 in s:
            current += 1
            length += 1

        longest = max(longest, length)

print("Longest Consecutive Length:", longest)

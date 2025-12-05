n = int(input())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

majority_found = False

for key in freq:
    if freq[key] > n // 2:
        print("Majority Element:", key)
        majority_found = True
        break

if not majority_found:
    print("No majority element")

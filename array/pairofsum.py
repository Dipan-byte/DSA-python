n = int(input())
arr = list(map(int, input().split()))
target = int(input())

seen = set()
found = False

for x in arr:
    if target - x in seen:
        print("Pair found:", target - x, x)
        found = True
        break
    seen.add(x)

if not found:
    print("No pair found")

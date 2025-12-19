n = int(input())
arr = list(map(int, input().split()))

min1 = None
min2 = None

for x in arr:
    if min1 is None or x < min1:
        min2 = min1
        min1 = x
    elif x != min1 and (min2 is None or x < min2):
        min2 = x

if min2 is None:
    print("No second smallest")
else:
    print("Second Smallest:", min2)

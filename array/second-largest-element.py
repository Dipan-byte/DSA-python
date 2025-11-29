n = int(input().strip())
arr = list(map(int, input().split()))

if n < 2:
    print("No second largest")
else:
    max1 = None  # largest
    max2 = None  # second largest

    for x in arr:
        if max1 is None or x > max1:
            max2 = max1
            max1 = x
        elif x != max1 and (max2 is None or x > max2):
            max2 = x

    if max2 is None:
        print("No second largest")
    else:
        print(max2)

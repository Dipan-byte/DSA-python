arr = [10, 45, 23, 89, 12]
max_element = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("Largest element =", max_element)

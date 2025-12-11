n1 = int(input())
a = list(map(int, input().split()))

n2 = int(input())
b = list(map(int, input().split()))

setA = set(a)
result = set()

for x in b:
    if x in setA:
        result.add(x)

print(*result)

lst = list(map(str, input().split()))
val = input()

for i in range(len(lst)):
    if lst[i] == val:
        lst[i] = "_"
print(lst)
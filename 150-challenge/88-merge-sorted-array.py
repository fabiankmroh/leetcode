# Input
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# List Concat
ccatlst = []
for item in num1 + num2:
    if item != 0:
        ccatlst.append(item)

for i in range(1, len(ccatlst)):
    if ccatlst[i-1] > ccatlst[i]:
        tmp = ccatlst[i-1]
        ccatlst[i-1] = ccatlst[i]
        ccatlst[i] = tmp

nums1 = ccatlst
print(nums1)

# Shows Fine Results on Local Compiler but Marked Wrong on LeetCode
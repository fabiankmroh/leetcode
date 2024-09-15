class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        finalArr = []
        finalArr.append(nums[0])

        for i in range(1, len(nums)):
            prev = nums[i-1]
            if prev == nums[i]:
                continue
            else:
                finalArr.append(nums[i])

        nums.clear()
        nums.extend(finalArr)

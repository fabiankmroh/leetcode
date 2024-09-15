class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        dropCnt = 0
        finalArr = []

        while i < len(nums):
            if nums[i] == val:
                dropCnt += 1
            else:
                finalArr.append(nums[i])

            #print('finalArr: ', finalArr)
            i += 1
        
        nums.clear()
        nums.extend(finalArr)

        return len(finalArr)

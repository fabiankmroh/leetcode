class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1 # nums1 Len Ref.
        j = n - 1 # nums2 Len Ref.
        k = m + n - 1 # Total Len Ref.
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: # Larger Number
                nums1[k] = nums1[i] # Placed at End
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while j >= 0: # Remaining in nums2
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


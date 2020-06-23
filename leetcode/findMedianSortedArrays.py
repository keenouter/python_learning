class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=list(set(nums1+nums2))
        nums3.sort()
        if len(nums3)%2==1:
            return nums3[int(len(nums3)/2)]
        else:
            return (nums3[int( len(nums3)/2)]+nums3[int(len(nums3)/2) - 1])/2

sol=Solution().findMedianSortedArrays([1,6],[4,10])
print(sol)
class Solution:
    def searchInsert(self, nums, target):
        # if target <= nums[0]:
        #     return 0
        # if target > nums[-1]:
        #     return len(nums)
        # n=len(nums)
        # mid=int(n/2)
        # while True:
        #     if target>nums[mid]:
        #         if target<=nums[mid+1]:
        #             return mid+1
        #         else:
        #             mid=int((mid+n)/2)
        #     elif target<nums[mid]:
        #         if target>=nums[mid-1]:
        #             return mid
        #         else:
        #             n=mid
        #             mid=int(mid/2)
        #     else:
        #         return mid
        # nums.append(target)
        # nums = sorted(nums)
        # return nums.index(target)

        return len([arg for arg in nums if arg <target])
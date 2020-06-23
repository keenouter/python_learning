class Solution:
    def threeSum(self, nums):
        nums.sort();
        list_set=list()
        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            elif nums[i]==0:
                if i+2<len(nums) and nums[i]+nums[i+1]+nums[i+2]==0:
                    list_set.append([0,0,0])
                else:
                    break
            else:
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]<0:
                        break
 
        return  list_set

sol=Solution().threeSum([0,-4,-1,-4,-2,-3,2])
print(sol)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict=dict()
        for i in nums:
            if str(i) in nums_dict.keys():
                nums_dict[str(i)]+=1
            else:
                nums_dict[str(i)]=1
        
        length=int(len(nums)/2)+1
        for key in nums_dict.keys():
            if nums_dict[key]>=length:
                return int(key)

    def majorityElement_1(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]

    
    def majorityElement_2(self, nums: List[int]) -> int:
        major_num=nums[0]
        count=1
        for i in range(len(nums)):
            if nums[i]==major_num:
                count+=1
            else:
                count-=1
                if count==0:
                    count=1
                    major_num=nums[i]
        return major_num
    
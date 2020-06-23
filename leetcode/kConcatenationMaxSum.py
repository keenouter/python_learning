class Solution:
    def kConcatenationMaxSum(self, arr, k):
        # max_index=0
        # max_child_sum=0
        # arr_sum=0
        # temp=0
        # min_sum=0
        # max_sum=0
        # for i in range(len(arr)):
        #     arr_sum+=arr[i]
        #     if temp>0:
        #         if temp>max_child_sum:
        #             max_child_sum=temp
        #             max_index=i
        #         temp+=arr[i]                
        #     elif temp<=0:
        #         if arr[i]<=0:
        #             temp=0
        #         else:
        #             temp=arr[i]
        #     if arr_sum<min_sum:
        #         min_sum=arr_sum
        #     if arr_sum>max_sum:
        #         max_sum=arr_sum
        # if temp>max_child_sum:
        #     max_child_sum=temp
        #     max_index= len(arr)
        # print(arr_sum,max_child_sum,temp)
        # return max([arr_sum*k-min_sum,arr_sum*(k-1)+sum(arr[:max_index])-min_sum,max_child_sum,temp+max_sum,0])
        arr_sum_list=[0]
        temp=0
        max_index=0
        max_sum=0
        for i in range(len(arr)):
            temp+=arr[i]
            if temp>max_sum:
                max_sum=temp
                max_index=i+1
            arr_sum_list.append(temp)
        left_min=min(arr_sum_list[:max_index-1])
        right_min=min(arr_sum_list[max_index+1:]+[0])
        
        return max([arr_sum_list[-1]*(k-1)+max_sum - left_min*2,])
        


print(Solution().kConcatenationMaxSum([1,2,3],3))
                


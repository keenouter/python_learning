## 大体的思路，二分法，先找到整个数组里最高的点，然后依此再找左边的最高点，依次左边向左，右边向右

def trap(heights):
    sum=0
    left_max = right_max = get_max(heights)

    ## 左边只往左走
    l_max = get_max(heights[:left_max])
    while l_max>0:
        for i in heights[l_max+1:left_max]:
            sum = sum+(heights[l_max]-i)
        left_max = l_max
        l_max = get_max(heights[:left_max])
    
    ## 右边往右走
    r_max = get_max(heights[right_max+1:])
    while r_max<len(heights)-1:
        for i in heights[right_max+1:r_max]:
            sum = sum+(heights[r_max]-i)
        right_max = r_max
        r_max = get_max(heights[right_max+1:])
    
    return sum



def get_max(heights):
    max =0
    if heights:
        for i in range(len(heights)):
            if heights[i]>=heights[max]:
                max=i
    return max

if __name__ =='__main__':
    a=[4,2,1,9,3,1,6]
    print(trap(a))


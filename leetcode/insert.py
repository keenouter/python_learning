# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。

# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

# 示例 1:

# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 示例 2:

# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/insert-interval
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        reconstructed=0
        for i in range(len(intervals)-1):
            #插入的新区间已经处理完毕
            if reconstructed==2:
                result.append(intervals[i])
            # 正在处理
            elif reconstructed==1:
                 if intervals[i][0]>newInterval[1]:
                    result.append(intervals[i])
                    result.append(newInterval)
                    reconstructed=2
                 elif intervals[i][1]>=newInterval[1]:
                    newInterval[1]=intervals[i][1]
                    result.append(newInterval)
                    reconstructed=2
            #h还没有找到新区间在原有区间的位置
            else:
                if i==0 and newInterval<intervals[i][0]:

                    if intervals[i][1]<newInterval[0]:
                        result.append(intervals[i])
                        if newInterval[0]<=intervals[i+1][0]:
                            reconstructed=1
                    elif intervals[i][0]<=newInterval[0]<=intervals[i][1]:
                        newInterval[0]=intervals[i][0]
                        reconstructed=1

        


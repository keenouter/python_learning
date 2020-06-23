class Solution:
    def spiralOrder(self, matrix):
        m=len(matrix)
        if m>1:
            n=len(matrix[0])
            result=[]
            if n>1:
                i=0
                while n-2*i>=1 or m-i*2>=1:
                    for k in range(i,n-i-1):
                        result.append(matrix[i][k])          
                    for q in range(i,m-i-1):
                        result.append(matrix[q][n-i-1])
                    for p in range(i,n-i-1):
                        result.append(matrix[m-i-1][n-p-1])
                    for r in range(i,m-i-1):
                        result.append(matrix[m-r-1][i])
                    i+=1
                if n-2*i==m-2*i:
                    result.append(matrix[i-1][i-1])
            elif n==1:
                for i in range(m):
                    result.append(matrix[i][0])
            return result
                    
        else:
            return matrix

test=[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
ll=Solution().spiralOrder(test)
print(ll)
# from collections import Counter
# colors = ['blue', 'red', 'blue', 'red', 'blue']
# counter = Counter(colors)
# counter['yellow'] += 1
# print(counter)
# counter.most_common()[0]
# print(counter.most_common()[0])
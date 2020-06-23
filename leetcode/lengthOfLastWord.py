class Solution:
    def lengthOfLastWord(self, s):
        length=0
        for i in range(len(s)):
            if s[len(s)-i-1].isalpha():
                length+=1
            else:
                if length>0:
                    break
        return length

print(Solution().lengthOfLastWord("b   a    "))
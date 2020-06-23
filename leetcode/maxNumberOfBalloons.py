class Solution:
    def maxNumberOfBalloons(self, text):
        if len(text) < 7:
            return 0
        digits_dict = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for i in range(len(text)):
            if text[i] in digits_dict.keys():
                if text[i] in ['l','o']:
                    digits_dict[text[i]] += 0.5
                else:
                    digits_dict[text[i]] += 1
        return int(min([value for value in digits_dict.values()]))

print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
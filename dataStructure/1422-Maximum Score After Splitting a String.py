class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 1
        score = 0

        sum = s.count('1')
        while right < len(s):

            left_score = s[:left+1].count('0')
            right_score = s[right:].count('1')
            score = max(score, left_score + right_score)
            left += 1
            right += 1
        return score

obj=Solution()
s = "01110"
obj.maxScore(s)
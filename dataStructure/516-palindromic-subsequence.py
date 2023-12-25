class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        subsequence = []

        for right in range(len(s)):
            subsequence.append(s[right])
            if subsequence != subsequence[::-1]:
                subsequence.pop()
        return len(subsequence)


obj=Solution()
s = "cbbd"
obj.longestPalindromeSubseq(s)
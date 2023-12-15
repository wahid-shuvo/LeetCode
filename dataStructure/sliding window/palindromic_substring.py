class Solution:
    def countSubstrings(self, s: str) -> int:

        def palindrome_check(s):
            return s == s[::-1]
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if palindrome_check(s[i:j+1]):
                    count+=1
        return count

obj=Solution()
s = "aaa"
print(obj.countSubstrings(s))
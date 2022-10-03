class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s)==sorted(t)

s = "a"
t = "ab"

obj = Solution()
if obj.isAnagram(s,t):
  print("true")
else:
  print("false")
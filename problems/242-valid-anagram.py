class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    t_dict={i:t[i] for i in range(len(t))}
    source=''
    for item in s:
      for k,v in t_dict.items():
        if item==v:
          source+=item
          t_dict.pop(k)
          break;
    if s==source and len(s)==len(t):
      return True
    else:
      return False

s = "a"
t = "ab"

obj = Solution()
if obj.isAnagram(s,t):
  print("true")
else:
  print("false")
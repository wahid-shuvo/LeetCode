class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    t_dict={}
    for item in t:
      t_dict[item]=t_dict.get(item,0)+1
    res=''
    for ch in s:
      for k,v in t_dict.items():
        if ch==k:
          res+=ch
          t_dict.pop(k)
          break;
    return res==s and len(s)==len(t)

s = "silent"
t = "slisten"

obj = Solution()
print(obj.isAnagram(s,t))
# if obj.isAnagram(s,t):
#   print("true")
# else:
#   print("false")
#
# t_dict = {i: t[i] for i in range(len(t))}
# source = ''
# for item in s:
#   for k, v in t_dict.items():
#     if item == v:
#       source += item
#       t_dict.pop(k)
#       break;
#
# if s == source and len(s) == len(t):
#   return True
# else:
#   return False
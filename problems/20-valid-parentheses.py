class Solution:
  def isValid(self, s: str) -> bool:
    temp_list=[]
    if len(s)%2==0:
      for item in s:
        if item=='(' or item=='{' or item=='[':
          temp_list.append(item)
        elif item==')':
          if len(temp_list) > 0:
            if temp_list.pop()!='(':
              return False
          else:
            return False
        elif item=='}':
          if len(temp_list) > 0:
            if temp_list.pop()!='{':
              return False
          else:
            return False
        elif item==']':
          if len(temp_list) > 0:
            if temp_list.pop()!='[':
              return False
          else:
            return False
      if len(temp_list)==0:
        return True
    else:
      return False


s ="))"
obj = Solution()

if obj.isValid(s):
  print('true')
else:
  print('false')

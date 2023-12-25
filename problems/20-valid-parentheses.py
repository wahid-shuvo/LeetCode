class Solution:
  def isValid(self, s: str) -> bool:
    map={')':'(','}':'{',']':'['}
    stack=[]
    for char in s:
      if char in map.keys():
        top_element=stack.pop() if stack else '#'
        if top_element!=map[char]:
          return False
      else:
        stack.append(char)
    return not stack


s =")"
obj = Solution()
print(obj.isValid(s))



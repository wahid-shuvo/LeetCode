from typing import List
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    freq = {}
    for item in nums:
      if item in freq:
        freq[item] += 1
      else:
        freq[item] = 1
    result=[]

    for val in nums:
      x=val
      for key,value in freq.items():
        y=key
        if x==y:
          if freq[x]<2:
            continue
        z=-(x+y)
        if x==y and y==z:
          if freq[x] >= 3 and (x+y+z)==0:
            result.append([x, y, z])
            continue
        elif z in freq:
          if y==z:
            if freq[z]>1:
              if (x+y+z)==0:
                result.append([x,y,z])
          elif x==z:
            if freq[z]>1:
              if (x+y+z)==0:
                result.append([x,y,z])
          else:
              if (x + y + z) == 0:
                result.append([x, y, z])

    final_result=[]
    for element in result:
      if sorted(element) not in final_result:
        final_result.append(sorted(element))

    return final_result

nums = [0,1,1]
obj = Solution()
print(obj.threeSum(nums))
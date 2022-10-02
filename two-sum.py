from typing import List
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    temp=sorted(nums)
    for i in range(len(nums)):
      a=nums[i]
      nums[i]=None
      temp.remove(a)
      search_element=target-a
      if search_element in temp:
        b=nums.index(search_element)
        if a+nums[b] == target:
          return [i,b]

nums=[3,3]
target=6
obj= Solution()
print(obj.twoSum(nums,target))
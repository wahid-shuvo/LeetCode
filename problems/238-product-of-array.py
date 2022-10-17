from typing import List
import math
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    result_prefix=[]
    prefix=1
    postfix=1
    size=len(nums)
    for i in range(size):
      result_prefix.append(prefix)
      prefix = prefix*nums[i]
    for i in range(-1,-size-1,-1):
      result_prefix[i]=result_prefix[i]*postfix
      postfix = postfix*nums[i]
    return result_prefix

nums=[1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))
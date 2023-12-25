from typing import List
import math
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    ans, pre, post = [1] * len(nums), 1, 1
    for i in range(len(nums)):
      ans[i], ans[-1 - i] = pre * ans[i], post * ans[-1 - i]
      pre, post = pre * nums[i], post * nums[-1 - i]
    return ans

nums=[1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))
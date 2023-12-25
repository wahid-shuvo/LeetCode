from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left = 0
        current_prod = 1
        max_prod = float('-inf')

        for right in range(len(nums)):
            current_prod *= nums[right]
            max_prod = max(max_prod, current_prod)

            if current_prod == 0:
                current_prod = 1
                left = right + 1
            elif current_prod < 0:
                while current_prod < 0:
                    current_prod //= nums[left]
                    left += 1

        return max_prod

obj=Solution()
nums = [-2,0,-1]
print(obj.maxProduct(nums))
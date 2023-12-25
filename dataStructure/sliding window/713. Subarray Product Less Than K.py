from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = ans=0
        current = 1

        if k<=1:
            return 0

        for right in range(len(nums)):
            current *= nums[right]
            while current >= 100:
                current/=nums[left]
                left+=1
            ans+=(right-left+1)
        return ans

obj=Solution()
nums = [10,5,2,6]
k = 100
ans=obj.numSubarrayProductLessThanK(nums,k)
print(ans)
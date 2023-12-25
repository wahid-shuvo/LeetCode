from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        left = right = ans = 0
        current_sum = 0

        if len(nums) <= 1:
            if nums[0] == k:
                return 1

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum>k and left<=right:
                current_sum-=nums[left]
                left+=1

            if current_sum==k:
                ans+=1
        return ans

obj=Solution()
nums = [1,2,3]
k = 3
ans=obj.subarraySum(nums,k)
print(ans)
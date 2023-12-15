from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]>nums[right]:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left+=1
            else:
                right-=1
                left+=1
obj=Solution()
nums = [2,0,1]
obj.sortColors(nums)
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        expected_nums = []
        for index in range(len(nums)):
            if nums[index] == val:
                nums[index] = '-'
            else:
                expected_nums.append(nums[index])

        count = len(expected_nums)
        sorted_expected_nums = sorted(expected_nums)

        item_count=0
        for item in range(len(nums)):
            if item_count<=len(sorted_expected_nums)-1:
                nums[item] = sorted_expected_nums[item]
                item_count += 1
            else:
                nums[item] ='-'
        return count


obj=Solution()
nums = [3,2,2,3]
val = 3
print(obj.removeElement(nums,val))

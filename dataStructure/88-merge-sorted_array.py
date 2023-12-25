from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_nums1=(m+n)-1

        if nums1 and nums2:
            for i in range(n):
                if nums1[left_nums1] == 0:
                    nums1[left_nums1] = nums2[i]
                    left_nums1 -= 1
        else:
            if nums1 and not nums2:
                pass
            else:
                nums1[0] = nums2[0]

        return nums1.sort()


obj=Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(obj.merge(nums1,m,nums2,n))






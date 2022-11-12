from typing import List
class Solution:
  def maxArea(self, height: List[int]) -> int:
    left_poniter=0
    right_pointer=len(height)-1
    max_area=0
    while(left_poniter<right_pointer):
      area=min(height[left_poniter],height[right_pointer])*abs((right_pointer-left_poniter))
      if area>max_area:
        max_area=area
      if height[left_poniter]<height[right_pointer]:
        left_poniter=left_poniter+1
      elif height[left_poniter]>height[right_pointer]:
        right_pointer=right_pointer-1
      else:
        left_poniter=left_poniter+1
        right_pointer=right_pointer-1
    return max_area

height=[1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))
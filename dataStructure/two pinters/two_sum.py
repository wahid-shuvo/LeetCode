def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    nums = sorted(nums)
    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return True
    return False


print(check_for_target([4, 5, 1, 3, 2, 6], 0))

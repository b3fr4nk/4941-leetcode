def searchInsert(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        m = (left + right) // 2
        if nums[m] >= target:
            prev_num = nums[m]
            right = m
        else:
            prev_num = nums[m]
            left = m + 1

    return left

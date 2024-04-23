def remove_element(nums, val):
    count = len(nums)
    i = 0
    while len(nums) > i:
        if nums[i] == val:
            count -= 1
            del nums[i]
        else:
            i += 1

    return count

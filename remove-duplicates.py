def removeDuplicates(nums):
    i = 1
    length = len(nums)
    while i < length:
        if nums[i] == nums[i-1]:
            del nums[i-1]
            length -= 1
        else:
            i += 1

    return length

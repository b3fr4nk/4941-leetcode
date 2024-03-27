def numSubarrayProductLessThanK(nums, k):
    index1 = 0
    index2 = 0
    prod = 1
    output = 0

    while index2 < len(nums):
        prod *= nums[index2]

        while index2 >= index1 and prod >= k:
            prod /= nums[index1]
            index1 += 1
        output += index2 - index1 + 1
        index2 += 1

    return output


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))

# 假设最大组数组为[i, ... k, ...j]
# sum([i,... , i]) = sum([i, ..., k]) + sum([k, ..., j])
# sum([i, ..., k]) = sum([i, ..., i]) - sum([k, ..., j]) >= 0
import sys

def find_max_subarray(nums):
    left = 0
    right = 0
    i = left
    j = right

    max_sum = -sys.maxsize - 1
    sum_now = 0

    while(j < len(nums)):
        sum_now += nums[j]
        if sum_now > max_sum: # 更新最大值
            max_sum  = sum_now
            left = i 
            right = j
        if sum_now < 0: # 如果当前值小于0，则重置
            sum_now = 0
            i = j + 1
        j += 1
    return nums[left:right + 1], max_sum

nums = [1, -2, 3, 10, -4, 7, 2, -5]
print(find_max_subarray(nums))

            
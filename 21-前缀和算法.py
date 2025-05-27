# 给出列表 recodes = [], 给出范围[minLen, maxLen], 给出阈值 baseLine
# 计算recodes里面长度在[minLen, maxLen]之间的，平均值>= baseLine 的子数组的数量

def finalist(recodes, minLen, maxLen, baseLine):
    n = len(recodes)
    prefix_sum = [0] * (n + 1)  # prefix_sum[i] 表示前recodes中前0到i - 1个元素的和
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + recodes[i - 1]
    res = 0
    for start in range(n):
        for end in range(minLen + start - 1, maxLen + 1):
            if (prefix_sum[end] - prefix_sum[start]) / (end - start) >= baseLine:
                res += 1
    
    return res
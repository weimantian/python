# 给出列表 recodes = [], 给出范围[minLen, maxLen], 给出阈值 baseLine
# 计算recodes里面长度在[minLen, maxLen]之间的，平均值>= baseLine 的子数组的数量

def finalist(recodes, minLen, maxLen, baseLine):
    n = len(recodes)
    prefix_sum = [0] * (n + 1)  # prefix_sum[i] 表示前recodes中前0到i - 1个元素的和
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + recodes[i - 1]
    print(prefix_sum)
    res = 0
    for start in range(n):
        for end in range(minLen + start - 1, maxLen + 1):
            length = end - start + 1
            sum = prefix_sum[end + 1] - prefix_sum[start]
            avg = sum / length
            if avg >= baseLine:
                print(recodes[start: end + 1])
                print(avg)
                res += 1
    return res
print(finalist([1,2,3,4,5,6], 3, 5, 2))

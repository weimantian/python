class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        res = float("inf")
        for start in range(0, n):
            for end in range(start, n):
                print(nums[start:end + 1])
                sum_t = prefix_sum[end + 1] - prefix_sum[start]
                length = end - start + 1
                if sum_t >= target:
                    if length < res:
                        res = length
        

        if res != float("inf"):
            return res
        else:
            return 0

                    
s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
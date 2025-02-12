"""
条件:需要计算子数组内不同元素的个数并更新
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        aim_dict = {}
        sum = 0
        "m is sum of different element "
        for index,value in enumerate(nums):
            if index < k - 1:
                sum += value
                if value not in aim_dict:
                    aim_dict[value] = 1
                else:
                    aim_dict[value] += 1
                continue
            sum += value
            if value not in aim_dict:
                aim_dict[value] = 1
            else:
                aim_dict[value] += 1
            # 判断是否满足条件
            if len(aim_dict) >= m:
                res = max(res, sum)
            sum -= nums[index - k + 1]
            aim_dict[nums[index - k + 1]] -= 1
            if aim_dict[nums[index - k + 1]] == 0:
                del aim_dict[nums[index - k + 1]]
        return res


if __name__ == '__main__':
    nums = [1,2,2]
    m = 2
    k = 2
    print(Solution().maxSum(nums,m,k))


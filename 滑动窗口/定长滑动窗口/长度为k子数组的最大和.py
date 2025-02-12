"""
需要判断所有元素各不相同
"""
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum = res = 0
        flag_dict = {}
        for index,value in enumerate(nums):
            if index < k-1:
                sum += value
                if value in flag_dict:
                    flag_dict[value] += 1
                else:
                    flag_dict[value] = 1
                continue
            sum += value
            if value in flag_dict:
                flag_dict[value] += 1
            else:
                flag_dict[value] = 1
            if len(flag_dict) == k:
                res = max(res,sum)
            sum -= nums[index-k+1]
            if flag_dict[nums[index-k+1]] == 1:
                del flag_dict[nums[index-k+1]]
            else:
                flag_dict[nums[index-k+1]] -= 1
        return res




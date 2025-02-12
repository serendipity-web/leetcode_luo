from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = i = ans = 0
        for j, num in enumerate(nums):
            if num == 0:
                cnt += 1
            while cnt > 1:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            ans = max(ans, j - i)
        return ans


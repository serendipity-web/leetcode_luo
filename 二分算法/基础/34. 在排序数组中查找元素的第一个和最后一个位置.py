from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 闭区间写法
        left = self._binary_search(nums, target)
        right = self._binary_search(nums, target + 1) - 1
        if nums[left] != target:
            return [-1, -1]
        return [left, right]

    def _binary_search(self, nums: List[int], target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                left = mid + 1
            elif nums[mid] < target:
                right = mid - 1
            else:
                right = mid - 1
        return left

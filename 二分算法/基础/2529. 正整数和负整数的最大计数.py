from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 找到小于0的的第一个参数与大于0的第一个参数，然后计算二者之间的最大值
        less_zero = self._binary_search(nums, 0)
        more_zero = self._binary_search(nums, 1)
        print(less_zero, more_zero)
        return max(less_zero +1, len(nums) - more_zero)

    def _binary_search(self, nums: List[int], target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == '__main__':
    nums = [5,20,66,1314]
    print(Solution().maximumCount(nums))
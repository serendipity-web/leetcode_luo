from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            # 找到第一个大于等于 success / spell 的 potion 的索引
            index = self.binary_search(potions, success / spell)
            res.append(len(potions) - index)
        return res
        # 复杂度
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    print(Solution().successfulPairs(spells, potions, success))
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        只需要考虑[arr1[i]-d,arr[i+d]是否在同一坐标即可
        """
        res = 0
        arr2.sort()
        for arr in arr1:
            p = self.binary_search(arr2, arr)
            if p == len(arr2) or abs(arr - arr2[p]) > d:
                if p == 0 or abs(arr - arr2[p - 1]) > d:
                    res += 1
        return res



    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        num = 0
        aim_num = k * threshold
        for i,n in enumerate(arr):
            num += n
            if i < k - 1:
                continue
            if num >= aim_num:
                res += 1
            num -= arr[i - k + 1]
        return res

if __name__ == '__main__':
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    print(Solution().numOfSubarrays(arr,k,threshold))


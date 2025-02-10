from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=-99999999999
        max_num = 0.0
        for i,n in enumerate(nums):
            max_num += n
            if i < k-1 :
                continue
            res = max(res,float(max_num/k))
            max_num -= nums[i-k+1]
        return res


if __name__ == '__main__':
    nums = [7,4,5,8,8,3,9,8,7,6]
    k = 7
    print(Solution().findMaxAverage(nums,k))

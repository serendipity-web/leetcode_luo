from typing import List
"""
计算n-k个数组的最小值
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        mid_res = 0
        res = 0
        max_sum = 9999
        if n == 0:
            return sum(cardPoints)
        for i in range(n):
            res += cardPoints[i]
        max_sum = mid_res
        for index,value in enumerate(cardPoints):
            if index < n-1:
                mid_res += value
            else:
                mid_res += value
                max_sum = min(mid_res,max_sum)
                mid_res -= cardPoints[index-n+1]
        return res - max_sum

if __name__ == '__main__':
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints,k))
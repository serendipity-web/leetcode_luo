# 如何判断i符合数组要求--->根据长度判断，每次遍历都要输出当前子数组的长度

# 用例分析:
# [7,4,3,9,1,8,5,2,6], k = 3

"""
1. 如何获取数组长度？
该步的输入为索引值i以及数组长度len and k,link is  len - i >= k
2. 实际需要考虑的子数组长度为子数组+后面k个
"""

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        s = 0  # 维护窗口元素和
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            if i < k * 2:  # 窗口大小不足 2k+1
                continue
            # 2. 记录答案
            avgs[i - k] = s // (k * 2 + 1)
            # 3. 离开窗口
            s -= nums[i - k * 2]
        return avgs


if __name__ == '__main__':
    nums = [8]
    k= 100000
    print(Solution().getAverages(nums,k))


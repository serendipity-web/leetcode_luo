"""
即是计算涂n-k 字符串所需要的数组的最小值

"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        end_res = len(blocks)
        for index,block in enumerate(blocks):
            if index < k-1:
                if block == 'W':
                    res += 1
                continue
            if block == 'W':
                res += 1
            end_res = min(end_res,res)
            if blocks[index-k+1] == 'W':
                res -= 1
        return end_res

if __name__ == '__main__':
    blocks = "WBBWWBBWBW"
    k = 7
    print(Solution().minimumRecolors(blocks,k))
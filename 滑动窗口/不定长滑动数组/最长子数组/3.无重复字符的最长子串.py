"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
s = "abcabcbb"

way:
在子字符串中每一个字符所在的位置
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        max_res = 0
        dict = {}
        for index,value in enumerate(s):
            if value in dict:
                '先记录长度'
                max_res = max(max_res,res)
                res = index - dict[value] + 1
                dict[value] = index
            else:
                dict[value] = index
                res += 1
                max_res = max(max_res,res)
        return  max_res

if __name__ == '__main__':
    s = "tmmzuxt"
    print(Solution().lengthOfLongestSubstring(s))

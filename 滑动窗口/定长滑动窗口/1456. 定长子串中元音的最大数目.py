class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):
           # 判断条件
            if c in 'aeiou':
                vowel += 1
           # 查询结界
            if i < k - 1:
                continue
           # 更新结果
            ans = max(ans, vowel)
           # 移除元素
            if s[i - k + 1] in 'aeiou':
                vowel -= 1
        return ans

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            print(i,-i-1)
            s[i],s[-i-1]=s[-i-1],s[i]

if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)

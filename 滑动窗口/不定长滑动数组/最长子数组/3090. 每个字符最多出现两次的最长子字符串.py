class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        #         和之前思路相同
        res = ans = 0
        aim_dict = {} #记录对应元素的次数
        index_dict= {}
        for index,value in enumerate(s):
            if value not in aim_dict:
                aim_dict[value] = 1
                index_dict[value] = index
                ans += 1
                res = max(res,ans)
            else:
                aim_dict[value] += 1
                index_dict[value] = index
                if aim_dict[value] > 2:
                    ans = index- index_dict[value]
                    aim_dict[value] = 2
                ans += 1
                res = max(res,ans)
        return res

if __name__ == '__main__':
    s = "bcbbbcba"
    print(Solution().maximumLengthSubstring(s))




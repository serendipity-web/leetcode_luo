from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        mid_res = 0
        length = len(code)
        num_iterations = 2  # 假设需要遍历两次

        for _ in range(num_iterations):
            for key, value in enumerate(code):
                if k == 0:
                    res.append(0)
                if key < k:
                    mid_res += value
                    continue
                res.append(mid_res)
                mid_res -= code[(key - k + length) % length]
                if len(res) == length:
                    break

        return res


if __name__ == '__main__':
    code = [5, 7, 1, 4]
    k = 3
    print(Solution().decrypt(code, k))
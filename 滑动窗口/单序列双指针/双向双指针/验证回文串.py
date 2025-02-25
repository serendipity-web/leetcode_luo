class Solution:
    def isPalindrome(self, s: str) -> bool:
        endres = ""
        for i in range(len(s)):
            if s[i].isalnum():
                endres += s[i].lower()
        for i in range(len(endres)//2):
            if endres[i] != endres[len(endres)-i-1]:
                return False
        return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"

    print(Solution().isPalindrome(s))
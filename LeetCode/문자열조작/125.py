# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if '0' <= i <= '9' or 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                tmp += i
        temp = tmp.lower()
        return temp == temp[::-1]

# S = Solution()
# S.isPalindrome("0P")
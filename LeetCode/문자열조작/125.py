# Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for i in s:
            if 0 <= ord(i) <= 127:
                tmp += i
        temp = tmp.lower()
        flag = True
        i, j = 0, len(temp)-1
        while i < j:
            if temp[i] != temp[j]:
                flag = False
                break
            i += 1
            j -= 1
        print(flag)
        return flag

S = Solution()
S.isPalindrome("0P")
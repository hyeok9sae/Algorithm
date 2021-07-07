# Reverse String
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        print(s)

S = Solution()
S.reverseString(["h","e","l","l","o"])
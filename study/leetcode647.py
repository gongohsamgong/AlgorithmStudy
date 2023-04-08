class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        for i in range(length):
            for j in range(i, length):
                if s[i:j] == s[j:i:-1]:
                    count += 1
        return count
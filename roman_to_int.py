#13 #HashTable #Math #String

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        return sum([romans[s[i]] if romans[s[i]] >= romans[s[i+1]] else -romans[s[i]] for i in range(len(s)-1)] + [romans[s[-1]]])
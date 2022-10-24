class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i, value in enumerate(s[:-1]):
            if d[s[i+1]] > d[s[i]]:
                res -= d[value]
            else:
                res += d[value]
        res += d[s[-1:]]

        return res

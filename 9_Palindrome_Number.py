class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = []
        num = ''
        for i in str(x):
            l.append(i)
        while len(l) > 0:
            print(l)
            num += l[-1]
            l.pop()
        return True if str(x) == num else False

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        while num >= 10:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp
        return num

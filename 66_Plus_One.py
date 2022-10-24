class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        string_num = ''.join(str(i) for i in digits)
        digits = [int(x) for x in str(int(string_num) + 1)]

        return digits

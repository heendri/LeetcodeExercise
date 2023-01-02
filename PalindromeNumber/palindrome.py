class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            
            reversed_num = 0
            temp_num = x
        
            while temp_num != 0:
                digit = temp_num % 10
                reversed_num = reversed_num * 10 + digit
                temp_num = temp_num //10
        
        return reversed_num == x
        
        # reversed_char = str(x)[::-1]
        # return str(x) == reversed_char
        
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = re.sub(r'[\W_]+', '', s)
        s=s.lower()
        # print(s)
        
#         reversed_string =""
        
#         for i in s:
#             reversed_string=i+reversed_string
        
        return s == s[::-1]
        

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        answer_list=[]
        def convert(list):
      
             # Converting integer list to string list
            s = [str(i) for i in list]
      
            # Join list items using join()
            res = int("".join(s))
      
            return(res)
        
        result = convert(digits) + 1
        
        for i in str(result):
            answer_list.append(int(i))
        
        return answer_list
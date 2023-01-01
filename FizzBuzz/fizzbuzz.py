class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer_list = []
        for x in range (1,n+1):
            if (x % 3 == 0 and x % 5 ==0):
                answer_list.append("FizzBuzz")
            elif x % 3 == 0:
                answer_list.append("Fizz")
            elif x % 5 == 0:
                answer_list.append("Buzz")
            else:
                answer_list.append(str(x))
        
        return answer_list
class Solution(object):
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def binary_to_decimals(binary):
            decimals = 0
            num_pow = 0
            for i in reversed(binary):
                if(binary[i] == str(1)):
                    decimals = decimals + (1*(2**num_pow))
                
                num_pow = num_pow + 1
            return decimals
        
        def decimals_to_binary(number):
            binary=""
            if number == 0:
                return "0"
            while number != 0:
                remainder = number % 2
                number = number // 2
                binary = str(remainder) + binary
            return binary
        
#         a = binary_to_decimals(a)
#         b = binary_to_decimals(b)
        
#         add_num = a + b
        
        return decimals_to_binary(binary_to_decimals(a) + binary_to_decimals(b))
        
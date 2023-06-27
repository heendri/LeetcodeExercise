class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums={}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] = dict_nums[i] + 1
        
        for x in dict_nums:
            if dict_nums[x] == 1:
                return x
            
        
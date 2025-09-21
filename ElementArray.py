class Solution(object):
    def searchRange(self, nums, target):
        s = []
        for i in range(len(nums)): 
                if nums[i] == target :  
                    s.append(i)
        
        return [s[0], s[-1]] if s else [-1, -1]


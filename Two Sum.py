class Solution(object):
    def twoseen(self, nums, target):
        seen = {}
        for i , num in enumerate(nums):
           complement = target - num  
           if complement in seen :
               return [seen[complement] , i]
           
           else:
               seen[num] = i 
               
            


sol = Solution()
print(sol.twoseen(nums = [3,3], target = 6))
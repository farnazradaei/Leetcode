class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for i , num in enumerate(numbers):
           complement = target - num  
           if complement in seen :
               return [seen[complement]+1 , i+1]
           
           else:
               seen[num] = i 
               
            


sol = Solution()
print(sol.twoSum(numbers = [-1,0], target = -1))

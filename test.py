class Solution(object):
    def Sum(self, nums, target):
        seen = {}
        tedad = 0
        for i , num in enumerate(nums) :
            comelet = target - num 
            if comelet in seen :
                tedad += 1 
                return [comelet , num ]
            
            else:
               seen[num] = i 
               

            

sol =  Solution()
print(sol.Sum(nums = [ 8 , 4 , 5 , 7 , 2] , target = 9 ))
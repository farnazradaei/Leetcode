class Solution(object):
    def twoSum(self, numbers, target):
        # Input: numbers = [2,7,11,15], target = 9 Output: [1,2]
        left = 0 
        right = len(numbers) - 1
        while left < right : 
            s = numbers[left]+ numbers[right]
            if s == target : 
                return [left+1 , right+1]     
            elif s < target : 
                left = left + 1 
            else :
                right = right - 1


sol = Solution()
print(sol.twoSum(numbers = [2,3,4], target = 6))
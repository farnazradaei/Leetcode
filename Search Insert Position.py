class Solution(object):
    def searchInsert(self, nums, target):
        left = 0 
        right = len(nums) - 1

        while left <= right :
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target : 
                left = mid + 1 
            else:
                right = mid - 1 

        return left
    
sol = Solution()
print(sol.searchInsert(nums = [1,3,4,5,6,7] , target = 2))


                



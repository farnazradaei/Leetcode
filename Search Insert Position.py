class Solution(object):
    def searchInsert(self, nums, target):
        for i, num in enumerate(nums):
            if target == num:
                return i
            elif target < num :
                return i
            
        return len(nums)


sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))
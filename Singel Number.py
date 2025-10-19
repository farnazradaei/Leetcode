class Solution(object):
    def singelNumber(self, nums):
        diff = {}
        for num in nums :
            if num in diff :
                diff[num] +=1
            else: 
                diff[num] = 1

        for key in diff :
            if diff[key] == 1 :
                return key
        

sol = Solution()
print(sol.singelNumber(nums =[4,1,2,1,2]))
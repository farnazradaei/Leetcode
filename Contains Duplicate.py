class Solution(object):
    def containsDuplicate(self, nums):
        tekrar = {}
        for num in nums :
            if num in tekrar:
                return(True)
        
            else:
                tekrar[num]=True
        return(False)
    

sol = Solution()
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

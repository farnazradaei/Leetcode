class Solution(object):
    def intersection(self, nums1, nums2):
        moshtrk = {}
        aaza = []
        for num in nums1 : 
            moshtrk [num] = nums1 
        for num in nums2 : 
            if num in moshtrk:
                if num not in aaza:
                    aaza.append(num)
                    
            
        return aaza

            


sol = Solution()
print(sol.intersection( nums1 = [1,2,2,1], nums2 = [2,2]))

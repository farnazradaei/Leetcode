class Solution(object):
    def intersection(self, nums1, nums2):
        moshtrk = {}
        aaza = []
        for num in nums1 : 
            if num in moshtrk:
                 moshtrk[num] += 1
            else : 
                 moshtrk[num] = 1 
        for num in nums2 : 
            if num in moshtrk and moshtrk[num] > 0 :
                aaza.append(num)
                moshtrk[num] -= 1

        return aaza

                   
        
sol = Solution()
print(sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))

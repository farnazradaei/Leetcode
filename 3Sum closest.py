class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # min_diff = float('inf')
        # closest_sum = 0
        # for i in range(len(nums)) :
        #     for j in range(i+1 , len(nums)) :
        #         for k in range(j+1, len(nums)) :
        #             s = nums[i] + nums[j] + nums[k]
        #             diff = abs(s - target)
        #             if diff < min_diff :
        #                 min_diff = diff
        #                 closest_sum = s

        # return closest_sum


        nums.sort()
        min_diff = float('inf')
        closest_sum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right :
                s = nums[i] + nums[left] + nums[right]
                diff = abs(s - target)
                if diff < min_diff :
                    min_diff = diff
                    closest_sum = s 

                if s == target :
                    return s
                if s < target :
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
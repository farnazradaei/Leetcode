"""
Project description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

nums=[3,2,4]
target= 6
found = False
for i in range(len(nums)) :
    for j in range (i+1 , len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])
            found= True
            break
    if found:
        break    



# https://leetcode.com/problems/contains-duplicate/
# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: trueInput
def Duplicate(nums,X):
    hset=set()
    for i in range(len(nums)):
        X = nums[i]   
        if X in hset:
            return True
        else:
            hset.add(X)
Input=[1,2,3,1]
output=Duplicate(Input,0) 
print(output)           
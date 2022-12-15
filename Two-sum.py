# https://leetcode.com/problems/two-sum/
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

def Twosum(nums,target):
    result=dict()
    for i in range(0,len(nums)):
        num = nums[i]
        compliment=target-num
        if num in result:
            return [result[num],i]
        else:
            result[compliment]=i
input=[1,8,7,5]
output=Twosum(input,15)
print(output)          
                   

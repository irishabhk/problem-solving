# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.

def kthSmallest(arr, l, r, k):
    for i in range(l,r):
        min_value=min(arr[i:])
        index_value=arr.index(min_value)
        arr[i],arr[index_value]=arr[index_value],arr[i]
    return arr[k-1]
   
inputArr=[7,10,4,3,20,15]
output = kthSmallest(inputArr,0,6,3)
print(output)

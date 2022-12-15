#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Input:
# N = 4
# Arr[] = {-1,-2,-3,-4}
# Output:
# -1
def Maxsubsum(Arr,l,n,output,max_sum):
    for i in range(n):
        max_sum = max_sum+Arr[i]
        if(max_sum > output):
            output = max_sum
        if (max_sum < 0):
            max_sum = 0 
    return output
input = [-1,-2,-3,-4]
OUT_PUT = Maxsubsum(input,0,4,float('-inf'),0)
print(OUT_PUT)             



        
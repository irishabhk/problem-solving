# Probelm URL: https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# Given an array (or string), the task is to reverse the array/string.
# Examples : 
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def reverse_array(start,end,A):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
        
    return A

A=["A","B","C",4,5,6]
print(A)
reverse_array(0,5,A)
print("reverse of the array")
print(A)
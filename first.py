def reverse_array(start,end,A):
    
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
        
    return
A=["A","B","C",4,5,6]
print(A)
reverse_array(0,5,A)
print("reverse of the array")
print(A)

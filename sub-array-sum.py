def maxsubsum(arr,l,n,out):
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            out=max(sum,out)        
    return out  
input = [-1,-2,-3,-4]
output = maxsubsum(input,0,4,-100000)
print(output)
          
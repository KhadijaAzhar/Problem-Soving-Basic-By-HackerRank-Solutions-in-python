#!/bin/python3


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr=0
    
    
   
    for i in range(0,len(arr)):
        sum_arr+=arr[i]
        
    sum_min=sum_arr-max(arr)
    sum_max=sum_arr-min(arr)
        
    print(sum_min,sum_max)
        

#if __name__ == '__main__':
arr = list(map(int, input("input array: ").rstrip().split()))

miniMaxSum(arr)


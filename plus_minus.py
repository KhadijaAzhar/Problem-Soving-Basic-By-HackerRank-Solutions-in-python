
# Complete the plusMinus function below.
def plusMinus(arr):
     sum_0=0
     sum_pos=0
     sum_neg=0
     for i in range(0,len(arr)):
        if arr[i]==0:
            sum_0=sum_0+1
        elif arr[i]>0:
            sum_pos=sum_pos+1
        elif arr[i]<0:
            sum_neg=sum_neg+1
            
    
     print("%f"%(sum_pos/ len(arr)))
     print("%f"%(sum_neg / len(arr)))
     print("%f"%(sum_0 / len(arr)))
        
#if __name__ == '__main__':
n = int(input("input array size :"))

arr = list(map(int, input("input array [positive negative and zero numbers] :").rstrip().split()))

plusMinus(arr)


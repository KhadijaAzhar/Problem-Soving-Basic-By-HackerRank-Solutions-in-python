def simpleArraySum(ar):
    #
    # Write your code here.
    sum=0
    for i in range(0,len(ar)):
        sum+=ar[i]
        
    return sum
    #


ar_count = int(input("input count of array "))

ar = list(map(int, input("input array ").rstrip().split()))

result = simpleArraySum(ar)

print("sum of array is :",result)

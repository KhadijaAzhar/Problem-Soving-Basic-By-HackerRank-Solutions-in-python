#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    sum_alice=0
    sum_bob=0
    
    for i in range(0,3):
        if a[i]>b[i]:
            sum_alice+=1
        if a[i]<b[i]:
            sum_bob+=1
    return [sum_alice,sum_bob]

#if __name__ == '__main__':
            
  
    #fptr = open(os.environ['HOME','/Sight/task_HackerRank/random_codes/compare_triplets'], 'w')

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(result)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

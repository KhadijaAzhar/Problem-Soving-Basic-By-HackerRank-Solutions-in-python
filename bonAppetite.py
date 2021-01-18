import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s=0
    for i in range(0,len(bill)):
        if k!=i:
            s+=bill[i]
    s=s/2
    if b !=s:
        print(int(b-s))
    else:
        print("Bon Appetit")
        

#if __name__ == '__main__':
nk = input().rstrip().split()

n = int(nk[0])
k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)

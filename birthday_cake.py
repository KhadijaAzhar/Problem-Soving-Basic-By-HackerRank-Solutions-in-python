#!/bin/python3

def birthdayCakeCandles(candles):

   sum_candles=0
    # Write your code here
   max_candle=max(candles)
   for i in range(0,len(candles)):
       if candles[i]==max_candle:
           sum_candles+=1
            
   return sum_candles


candles_count = int(input("Input number of cost").strip())

candles = list(map(int, input("Input candles").rstrip().split()))

result = birthdayCakeCandles(candles)


   

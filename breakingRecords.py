def breakingRecords(scores):
    max_sc=scores[0]
    min_sc=scores[0]
    max_score=min_score=0

    for i in range(1,len(scores)):
        if scores[i]>max_sc:
            max_sc=scores[i]
            max_score+=1
        if scores[i]<min_sc:
            min_sc=scores[i]
            min_score+=1 
    
    return [max_score ,min_score]

n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)


   

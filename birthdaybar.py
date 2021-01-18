def birthday(s, d, m):
    
    return sum([1 for i in range(n) if sum(s[i:i+m])==d])
        
        

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)
print(result)


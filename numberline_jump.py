def kangaroo(x1, v1, x2, v2):
   
    count = 1
    while x1 != x2 and count < 10000:
        count += 1
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return "YES"

        elif count == 10000:
            return "NO"

 
        
    


x1V1X2V2 = input("enter [x1 v1 x2 v2] : ").split()

x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)

print(result)

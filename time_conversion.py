def timeConversion(s):
    if s[-2:]== "AM" and s[:2]=="12":
        s_new="00"+s[2:8]
    
    elif s[-2:] == "AM": 
        s_new=s[:-2] 
        
    elif s[-2:]=="PM" and s[:2]=="12":
        s_new=s[:-2]
        
    else:
        s_new=str(int(s[:2])+12)+s[2:8]
    #
    # Write your code here.
    return s_new
    #

s = input("Input time in 12 hour clock format : ")

result = timeConversion(s)

print(result)

    

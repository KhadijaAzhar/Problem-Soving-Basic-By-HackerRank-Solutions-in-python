def gradingStudents(grades):
   # grades_new=[]
    for i in range(len(grades)):
        if grades[i]>37 and (grades[i]%5)!=0 and (5-(grades[i]%5))<3:
            grades[i]=grades[i]+(5-(grades[i]%5))
    return  grades
    # Write your code here


grades_count = int(input("enter student count for grades").strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print(result)

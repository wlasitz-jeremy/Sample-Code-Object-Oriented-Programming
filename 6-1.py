RC='Rock Climbing'
print(RC[5:10])
for height in range(0,len(RC)):
    print(RC[height-8])


height=0
while height<len(RC):
    print(RC[height])
    height+=2
print(RC.upper())
print(RC.lower())


course=input("Enter course name: ")
alpha=0
digit=0
for letter in course:
    if course.isalpha():
        alpha+=1
    else:
        if course.isalnum():
            digit+=1
print(alpha,digit)












































































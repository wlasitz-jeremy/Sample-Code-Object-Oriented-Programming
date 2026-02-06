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
beta=0
charlie=0
for charlie in course:
    if course.isalpha():
        alpha+=1
    else:
        if course.isalnum():
            beta+=1
print(alpha,beta)


slide 21 practice task









































































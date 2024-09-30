n=int(input("Enter number of students\n"))
for i in range(n):
    stu_id=input("Enter student id\n")
    stu_name=input("Enter student name\n")
    m1=int(input("Enter sub1 marks\n"))
    m2=int(input("Enter sub2 marks\n"))
    m3=int(input("Enter sub3 marks\n"))
    total=m1+m2+m3
    print("*******STUDENT DETAILS*******")
    print("STUDENT ID:",stu_id)
    print("STUDENT NAME:",stu_name)
    print("TOTAL MARKS:",total,"\n")
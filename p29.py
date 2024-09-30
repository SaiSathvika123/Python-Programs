f=open("Student details.txt","a")
n=int(input("Enter no.of students:\n"))
for i in range(n):
    stu_id=input("Enter student id:\n")
    stu_nm=input("Enter student name:\n")
    scl_nm=input("Enter school name:\n")
    sub1=int(input("Enter sub1 marks:\n"))
    sub2=int(input("Enter sub2 marks:\n"))
    total=sub1+sub2
    
    str1=stu_id+'#'+stu_nm+'#'+scl_nm+'#'+str(total)+'\n'
    f.write(str1)
    print("student details enrolled")
f.close()

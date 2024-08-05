c_id=input("Enter student id\n")
name=input("Enter student name\n")
m1=int(input("Enter sub1 marks\n"))
m2=int(input("Enter sub2 marks\n"))
m3=int(input("Enter sub3 marks\n"))
total=m1+m2+m3
res=[]
res.append(c_id)
res.append(name)
res.append(m1)
res.append(m2)
res.append(m3)
res.append(total)
print("********STUDENT DETAILS********")
print(res)




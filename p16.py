n=int(input("Enter no.of students:"))
for i in range(n):
    fname=input("Enter student firstname:\n")
    lname=input("Enter student secondname:\n")
    name=fname+lname
    gender=input("Enter gender:\n")
    scl_name=input("Enter school name:\n")
    sub1=input("Enter sub1 marks:\n")
    sub2=input("Enter sub2 marks:\n")
    res=[]
    res.append(name)
    res.append(gender.upper())
    res.append(scl_name)
    res.append(sub1)
    res.append(sub2)
    res1='#'.join(res)
    print("STUDENT DETAILS")
    print(res1)

f=open("Person details.txt","a")
n=int(input("Enter no.of persons:\n"))
for i in range(n):
    name=input("Enter person name:\n")
    gender=input("Enter gender:\n")
    num=int(input("Enter mobile number:\n"))
    m=int(input("Enter no.of languages:\n"))
    langs=[]
    for j in range(m):
        lang=input("Enter language:\n")
        langs.append(lang)
    lst1=['male','Male','MALE']
    lst2=['female','Female','FEMALE']
    if gender in lst1:
        gender='M'
    elif gender in lst2:
        gender='F'
    langs_str='#'.join(langs)
    str1=name+','+gender+','+str(num)+','+langs_str+'\n'
    f.write(str1)
    print("Person details enrolled")
f.close()

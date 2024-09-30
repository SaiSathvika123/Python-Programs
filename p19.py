fname=input("Enter the first name:\n")
lname=input("Enter the last name:\n")
name=fname+lname
gender=input("Enter gender:\n")
Mobile=input("Enter mobile number:\n")
n=int(input("Enter languages known:\n"))
langs=[]
for i in range(n):
    lang=input("Enter language\n")
    langs.append(lang.upper())
pancard=input("Enter pancard:\n")
print("NAME:",fname.capitalize()+lname.capitalize())
lst1=['male','Male','MALE']
lst2=['female','Female','FEMALE']
if gender in lst1:
    print("GENDER: M")
elif gender in lst2:
    print("GENDER: F")
if len(Mobile)==10:
    print("MOBILE NUMBER:",Mobile)
print("LANGUAGES:",langs)
if len(pancard)==10 and pancard[:5].isalpha() and pancard[-1].isupper():
    print("PANCARD:",pancard)

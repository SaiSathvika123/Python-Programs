movies = ['sahoo','robo','saira','raja','krish','andarivadu']
lst1=[]
lst2=[]
lst=[]
for movie in movies:
    if len(movie)==4:
        lst1.append(movie)
    elif len(movie)==5:
        lst2.append(movie)
    else:
        lst.append(movie)
print(lst1)
print(lst2)
print(lst)

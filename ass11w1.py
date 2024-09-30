lst=[]
for i in range(7):
    if i in (3,6):
        continue
    else:
        lst.append(i)
print(lst)

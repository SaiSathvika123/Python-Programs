lst1=[1,2,3,4,5,6]
lst2=[1,3,7,9,4]
res=[]
for i in lst1:
    if i not in lst2:
        res.append(i)
print(res)

str1='AB10OBCD200C300'
res=[]
for i in str1:
    if i.isalpha():
        res.append(i)
print(''.join(res))

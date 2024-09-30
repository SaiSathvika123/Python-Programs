dict1={
    'B1':['apple','banana','cherry'],
    'B2':['mango','cherry','pineapple'],
    'B3':['apple','mango'],
    'B4':['pineapple','banana']
    }
res=[]
for v in dict1.values():
    for i in v:
        res.append(i)
lst=set(res)
for item in lst:
    res=[]
    for k,v in dict1.items():
        if item in v:
            res.append(k)
    print(item,res)

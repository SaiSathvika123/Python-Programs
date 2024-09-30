server_dtls={
    'dev':['user1','user2','user3','user4'],
    'test':['user2','user3'],
    'prod':['user1','user3','user4'],
    }
res=[]
for v in server_dtls.values():
    for i in v:
        res.append(i)
lst=set(res)
for item in lst:
    res=[]
    for k,v in server_dtls.items():
        if item in v:
            res.append(k)
    print(item,res)

acct_dtls={
    '101,srinivas,HDFC,Madhapur',
    '102,sriram,ICICI,Kondapur',
    '103,srikar,HDFC,Madhapur'
    }
print("****Bank Details****")
for item in acct_dtls:
    r_lst=item.split(',')
    #print(r_lst)
    print("Acount id:",r_lst[0])
    print("Account name:",r_lst[1])
    print("Bank name:",r_lst[2])
    print("Branch name:",r_lst[3],"\n")

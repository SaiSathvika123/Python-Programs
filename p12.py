prd_nm=input("Enter product name\n")
prd_prc=int(input("Enter product price\n"))
prd_qt=int(input("Enter prodduct quantity\n"))
total=prd_prc*prd_qt
prd_dtls={}
prd_dtls['PROD_NAME']=prd_nm
prd_dtls['PROD_PRICE']=prd_prc
prd_dtls['Quantity']=prd_qt
prd_dtls['TOTAL']=total
print("PRODUCT DETAILS",prd_dtls)

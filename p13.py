n=int(input("Enter no.of vegetables\n"))
res=[]
for i in range(n):
    vg_nm=input("Enyter vegetable name\n")
    vg_pc=int(input("Enter price per kg\n"))
    vg_kg=int(input("Enter no.of kgs\n"))
    price=vg_pc*vg_kg
    vg_dtls={}
    vg_dtls[vg_nm]=price
    res.append(vg_dtls)
print("VEGETABLE DETAILS",res)
    
    

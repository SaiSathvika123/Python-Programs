lst1=[7,5,18,21,6,4,36]
n=len(lst1)
for i in range(n):
    for j in range(i+1,n):
        if lst1[i]>lst1[j]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
print(lst1)

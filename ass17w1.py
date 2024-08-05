lst = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999]
leap_lst=[]
for year in lst:
    if year%4==0:
        leap_lst.append(year)
print(leap_lst)

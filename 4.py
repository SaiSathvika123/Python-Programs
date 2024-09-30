#a={1,6,3,"sai"}
#print(type(a))
#a.add(78)
#print(a)
#a.remove(1)
#print(a)
#def fact(n):
 #   if n==1 or n==0:
  #      return 1
   # else:
    #    return n*fact(n-1)
#x=fact(5)
#print(x)
def sum(*args):
    sm=0
    for i in args:
        sm+=i
    print(sm)
sum(4,5,2,8,23)


        

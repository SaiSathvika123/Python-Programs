#def printDivisors(n):
 #   for i in range(1,n+1):
  #      if n%i==0:
   #         print(i,end=" ")
    # Write your code here
#n=int(input())
#printDivisors(n)
from typing import List

def printDivisors(n: int) -> List[int]:
    divisors = []
    
    # Iterate over all possible divisors from 1 to sqrt(N)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    # Sort the list of divisors in ascending order
    divisors.sort()
    
    # Implementing pass as requested
    pass
    
# Example usage:
N = int(input().strip())

divisors = printDivisors(N)
print(" ".join(map(str, divisors)))

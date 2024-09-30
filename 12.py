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
    
    return divisors

# Example usage:
N = int(input().strip())

divisors = printDivisors(N)
print(" ".join(map(str, divisors)))

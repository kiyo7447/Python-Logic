"""
This module calculates perfect numbers using Mersenne primes. A perfect number is a positive integer that is equal to the sum of its proper divisors. 
The formula for a perfect number given a Mersenne prime is 2^(p-1) * (2^p - 1), where p is the prime number used in the Mersenne prime.
The module calculates the seventh and eighth perfect numbers using p = 19 and p = 31 respectively. It also provides a function to calculate the nth perfect number.
"""

# To find the seventh perfect number, we need to find the seventh Mersenne prime first.
# The formula for a perfect number given a Mersenne prime is 2^(p-1) * (2^p - 1),
# where p is the prime number used in the Mersenne prime.

# The first seven Mersenne primes are for p = 2, 3, 5, 7, 13, 17, 19.
# We will calculate the seventh perfect number using p = 19.

p = 19
seventh_perfect_number = (2 ** (p - 1)) * (2 ** p - 1)

print(seventh_perfect_number)
# 137438691328

p = 31
eighth_perfect_number = (2 ** (p - 1)) * (2 ** p - 1)
eighth_perfect_number

print(eighth_perfect_number)

def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def perfect_number(p):
    """
    This function calculates the nth perfect number using the formula 2^(p-1) * (2^p - 1), where p is the prime number used in the Mersenne prime.
    
    Args:
    p (int): The prime number used in the Mersenne prime.
    
    Returns:
    int: The nth perfect number.
    """
    return (2 ** (p - 1)) * (2 ** p - 1)

t = 1
for i in range(1, 101):
    a = perfect_number(i)
    if a == sum_divisors(a):
        print(f'{t}th perfect number is {a}')
        t += 1

"""
1th perfect number is 6
2th perfect number is 28
3th perfect number is 496
4th perfect number is 8128
5th perfect number is 33550336
"""

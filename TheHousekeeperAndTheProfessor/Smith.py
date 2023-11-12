def is_smith_number(n):
    """
    Return True if n is a Smith number, False otherwise.
    """
    # Find the prime factors of n
    factors = []
    n1 = n
    d = 2
    while d * d <= n1:
        while (n1 % d) == 0:
            factors.append(d)
            n1 //= d
        d += 1
    if n1 > 1:
        factors.append(n1)

    # Return False if n is a prime number
    if len(factors) == 1:
        return False

    # Calculate the sum of the digits of the prime factors
    digit_sum = 0
    for factor in factors:
        for digit in str(factor):
            digit_sum += int(digit)

    # Calculate the sum of the digits of n
    n_digit_sum = 0
    for digit in str(n):
        n_digit_sum += int(digit)

    # Return True if the digit sums are equal, False otherwise
    return digit_sum == n_digit_sum

i = 5
print(f'{i} is smith: {is_smith_number(i)}')
i = 22
print(f'{i} is smith: {is_smith_number(i)}')

def enumerate_smith_numbers(limit):
    """
    Enumerate all Smith numbers up to the given limit.
    """
    smith_numbers = []
    n = 4
    while len(smith_numbers) < limit:
        if is_smith_number(n):
            smith_numbers.append(n)
        n += 1
    return smith_numbers    

# パラメータの数字を素因数分解する関数
def prime_factorization(n):
    """
    Return the prime factorization of n as a list of prime factors.
    """
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

for i in enumerate_smith_numbers(100000):
    print(f'num:{i} factor:{prime_factorization(i)}')


i = 49_377_775
print(f'{i} is smith: {is_smith_number(i)}')
i = 5_000_011 
print(f'{i} is smith: {is_smith_number(i)}')
i = 50_000_017
print(f'{i} is smith: {is_smith_number(i)}')


"""
num:4 factor:[2, 2]
num:22 factor:[2, 11]
num:27 factor:[3, 3, 3]
num:58 factor:[2, 29]
num:85 factor:[5, 17]
num:94 factor:[2, 47]
num:121 factor:[11, 11]
num:166 factor:[2, 83]
num:202 factor:[2, 101]
num:265 factor:[5, 53]
num:274 factor:[2, 137]
num:319 factor:[11, 29]
num:346 factor:[2, 173]
num:355 factor:[5, 71]
num:378 factor:[2, 3, 3, 3, 7]
num:382 factor:[2, 191]
num:391 factor:[17, 23]
num:438 factor:[2, 3, 73]
num:454 factor:[2, 227]
num:483 factor:[3, 7, 23]
num:517 factor:[11, 47]
num:526 factor:[2, 263]
num:535 factor:[5, 107]
num:562 factor:[2, 281]
num:576 factor:[2, 2, 2, 2, 2, 2, 3, 3]
num:588 factor:[2, 2, 3, 7, 7]
num:627 factor:[3, 11, 19]
num:634 factor:[2, 317]
num:636 factor:[2, 2, 3, 53]
num:645 factor:[3, 5, 43]
num:648 factor:[2, 2, 2, 3, 3, 3, 3]
num:654 factor:[2, 3, 109]
num:663 factor:[3, 13, 17]
num:666 factor:[2, 3, 3, 37]
num:690 factor:[2, 3, 5, 23]
num:706 factor:[2, 353]
num:728 factor:[2, 2, 2, 7, 13]
num:729 factor:[3, 3, 3, 3, 3, 3]
num:762 factor:[2, 3, 127]
num:778 factor:[2, 389]
num:825 factor:[3, 5, 5, 11]
num:852 factor:[2, 2, 3, 71]
num:861 factor:[3, 7, 41]
num:895 factor:[5, 179]
num:913 factor:[11, 83]
num:915 factor:[3, 5, 61]
num:922 factor:[2, 461]
num:958 factor:[2, 479]
num:985 factor:[5, 197]
num:1086 factor:[2, 3, 181]
num:1111 factor:[11, 101]
num:1165 factor:[5, 233]
num:1219 factor:[23, 53]
num:1255 factor:[5, 251]
num:1282 factor:[2, 641]
num:1284 factor:[2, 2, 3, 107]
num:1376 factor:[2, 2, 2, 2, 2, 43]
num:1449 factor:[3, 3, 7, 23]
num:1507 factor:[11, 137]
num:1581 factor:[3, 17, 31]
num:1626 factor:[2, 3, 271]
num:1633 factor:[23, 71]
num:1642 factor:[2, 821]
num:1678 factor:[2, 839]
num:1736 factor:[2, 2, 2, 7, 31]
num:1755 factor:[3, 3, 3, 5, 13]
num:1776 factor:[2, 2, 2, 2, 3, 37]
num:1795 factor:[5, 359]
num:1822 factor:[2, 911]
num:1842 factor:[2, 3, 307]
num:1858 factor:[2, 929]
num:1872 factor:[2, 2, 2, 2, 3, 3, 13]
num:1881 factor:[3, 3, 11, 19]
num:1894 factor:[2, 947]
num:1903 factor:[11, 173]
num:1908 factor:[2, 2, 3, 3, 53]
num:1921 factor:[17, 113]
num:1935 factor:[3, 3, 5, 43]
num:1952 factor:[2, 2, 2, 2, 2, 61]
num:1962 factor:[2, 3, 3, 109]
num:1966 factor:[2, 983]
num:2038 factor:[2, 1019]
num:2067 factor:[3, 13, 53]
num:2079 factor:[3, 3, 3, 7, 11]
num:2155 factor:[5, 431]
num:2173 factor:[41, 53]
num:2182 factor:[2, 1091]
num:2218 factor:[2, 1109]
num:2227 factor:[17, 131]
num:2265 factor:[3, 5, 151]
num:2286 factor:[2, 3, 3, 127]
num:2326 factor:[2, 1163]
num:2362 factor:[2, 1181]
num:2366 factor:[2, 7, 13, 13]
num:2373 factor:[3, 7, 113]
num:2409 factor:[3, 11, 73]
num:2434 factor:[2, 1217]
num:2461 factor:[23, 107]
num:2475 factor:[3, 3, 5, 5, 11]
num:2484 factor:[2, 2, 3, 3, 3, 23]
"""
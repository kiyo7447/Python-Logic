def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

for i in range(1, 100000):
    if sum_divisors(i) == i:
        print(i)

# 6
# 28
# 496
# 8128


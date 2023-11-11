def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

for i in range(1, 100001):
    if sum_divisors(sum_divisors(i)) == i and i != sum_divisors(i):
        print(f'i={i}, p={sum_divisors(i)}')

# i=220, p=284
# i=284, p=220
# i=1184, p=1210
# i=1210, p=1184
# i=2620, p=2924
# i=2924, p=2620
# i=5020, p=5564
# i=5564, p=5020
# i=6232, p=6368
# i=6368, p=6232
# i=10744, p=10856
# i=10856, p=10744
# i=12285, p=14595
# i=14595, p=12285
# i=17296, p=18416
# i=18416, p=17296
# i=63020, p=76084
# i=66928, p=66992
# i=66992, p=66928
# i=67095, p=71145
# i=69615, p=87633
# i=71145, p=67095
# i=76084, p=63020
# i=79750, p=88730
# i=87633, p=69615
# i=88730, p=79750

# ハッピー数をもとめるプログラム

# Purpose: Check if a number is happy or not
def is_happy_number(n):
    seen = set()
    while n != 1:
        n = sum(int(digit)**2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
        # print(seen)
    return True

def find_consecutive_happy_numbers(count):
    consecutive_count = 0
    i = 1
    while consecutive_count < count:
        if is_happy_number(i):
            consecutive_count += 1
        else:
            consecutive_count = 0
        i += 1
    return i - count

for count in range(2, 8):
    print(f"The first number with {count} consecutive happy numbers is {find_consecutive_happy_numbers(count)}")


"""
The first number with 2 consecutive happy numbers is 31
The first number with 3 consecutive happy numbers is 1880
The first number with 4 consecutive happy numbers is 7839
The first number with 5 consecutive happy numbers is 44488
"""


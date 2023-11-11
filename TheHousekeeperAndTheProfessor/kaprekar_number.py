"""
カプレカ数とは、特別な性質を持つ数字のことです。例えば、数を2乗（かける）したときに、その結果を2つの部分に分け、それを足し合わせると、もとの数に戻る数字のことを指します。

例として、9を見てみましょう。9を2乗すると、
9 × 9 = 81
9×9=81 になります。この81を二つに分けて（8と1に分ける）、それを足し合わせると、
8 + 1 = 9
8+1=9 となり、もとの数の9に戻ります。だから、9はカプレカ数です。
"""

def is_kaprekar_number(n):
    """
    Check if a number is a Kaprekar number.
    A number is a Kaprekar number if its square can be split into two parts
    that add up to the original number.
    """
    square = n * n
    str_square = str(square)
    len_str_square = len(str_square)

    for i in range(1, len_str_square):
        part1 = int(str_square[:i])
        part2 = int(str_square[i:])

        # Avoid the case where part2 begins with 0s as it is not a valid split
        if str_square[i] == '0':
            continue

        if part1 + part2 == n:
            return True

    return False

# Find Kaprekar numbers in a certain range
kaprekar_numbers = [n for n in range(1, 10001) if is_kaprekar_number(n)]
kaprekar_numbers[:10]  # Display the first 10 Kaprekar numbers for brevity

print(kaprekar_numbers[:10]) 

"""
[9, 45, 55, 297, 703, 2223, 2728, 4950, 5050, 7272]
"""
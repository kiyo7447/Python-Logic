def is_kaprekar_number(n):
    if n == 1:
        return True
    else:
        square = str(n**2)
        for i in range(1, len(square)):
            left = int(square[:i])
            right = int(square[i:])
            if left != 0 and right != 0 and left + right == n:
                return True
    return False


i = 6174
print(f'Is {i} a Kaprekar number? {is_kaprekar_number(i)}')



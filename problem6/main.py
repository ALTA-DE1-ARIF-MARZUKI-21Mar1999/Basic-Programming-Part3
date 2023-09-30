def full_prima(N):
    # your code here
    if N <= 0:
        return False

    def prima(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    while N > 0:
        digit = N % 10
        if not prima(digit):
            return False
        N //= 10
    return True

if __name__ == '__main__':
    print(full_prima(2))  # True
    print(full_prima(3))  # True
    print(full_prima(11))  # False
    print(full_prima(13))  # False
    print(full_prima(23))  # True
    print(full_prima(29))  # False
    print(full_prima(37))  # True
    print(full_prima(41))  # False
    print(full_prima(43))  # False
    print(full_prima(53))  # True
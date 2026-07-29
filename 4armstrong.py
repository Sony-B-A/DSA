# Armstrong number
# level: Easy

def armstrong(num):
    if num < 0:
        return False

    n = num
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    n = num
    res = 0
    while n > 0:
        ld = n % 10
        res = res + ld ** count
        n = n // 10

    return res == num

"""def digit_sum(n):
    total = 0
    n = str(n)
    for i in range(len(n)):
        total += int(n[i])
    return total
print digit_sum (65)"""

def digit_sum(n):
    total = 0
    while n // 10 >= 1:
        n_r = n % 10
        n = n // 10
        total += n_r 
    total += n
    return total
print digit_sum (123)

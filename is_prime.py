def is_prime(x):
    x = abs(x)
    result = None
    """if x == 0 or x == 1:
        result = False
        return result"""
    for n in range(2, x-1):
        if x % n == 0:
            result = False
            break
            
    else:
        result = True
    return result

y = (is_prime(2))
print (y)

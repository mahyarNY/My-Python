def shift (key, array):
    return array[-key:] + array[:-key]
a = [1, 0, 0, 0]

print (shift(1, a))


def purify(list_purify):
    list_new = []
    for i in list_purify:
        if i % 2 != 0:
            list_new = list_purify.remove(i)
    return list_new

my_list = [1, 2, 4, 7]
print purify(my_list)

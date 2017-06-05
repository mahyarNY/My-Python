def remove_duplicates(list_):
    count = 1
    for item in list_:
        while count <= len(list_):
            if item == list_[count]:
                list_.remove(list_[count])
            count += 1
    return list_

print (remove_duplicates([1, 2, 2, 1]))

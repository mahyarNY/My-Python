def remove_duplicates(list_):
    turn = 0
    index_list = []
    for item in list_:
        count = 1 + turn
        while count < len(list_):
            if item == list_[count]:
                index_list.append(list_.index(list_[count]))
            count += 1
        turn += 1
    for e in index_list:
        list_.remove(list_[e])
    return list_

print (remove_duplicates([1, 2, 2, 1]))


def purify(list_):
    list_new = []
    index_list = []
    no_list = []
    for i in list_:
        if i % 2 != 0:
            index_list.append(list_.index(i))
        
    for e in index_list:
        no_list.append(list_[e])
    for item in list_:
        if item not in no_list:
            list_new.append(item)
    return list_new

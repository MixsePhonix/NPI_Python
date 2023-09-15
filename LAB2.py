def lots_of_list(lists):
    new_lists = []
    for i in lists:
        new_list = list(i)
        new_lists.append(new_list)

    return new_lists


list1 = ('amogus', 'sus', 'sos')

result = lots_of_list(list1)
for j in result:
    print(j)


def lots_of_list(lists):
    new_lists = []
    for i in lists:
        new_lists.append(i)

    return new_lists


list1 = ('amogus', 'sus', 'sos')

result = lots_of_list(list1)
for j in result:
    print(j)

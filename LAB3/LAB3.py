def list_of_lists(list):
    lists = [element for sublist in list for element in sublist]
    return lists


list_of_list = [[2, 6, 'amogus'], [4, True, 'no'], ['yes', 5, 7]]
Final_list = list_of_lists(list_of_list)
print(Final_list)

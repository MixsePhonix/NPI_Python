import json

data_file = 'DATA.txt'


def dictionary_to_json(dic):

    new_dic = {}

    for key, value in dic.items():
        if isinstance(value, list) and all(isinstance(item, int) for item in value):
            new_dic[key] = value

    with open('DATA.txt', 'w') as outfile:
        json.dump(new_dic, outfile)
    return


data = {'amogus': [1, 6, 3, 6],
        'amo': 'data',
        'imposter': [2, 6, 7, 2],
        'answer': True,
        'password': [2, 7, 2, 7, 7, 7],
        'name': [1, 'z', 6, 'x']
        }

dictionary_to_json(data)

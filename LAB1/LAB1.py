def adding_objects(obj1, obj2):
    newObj = {}

    for i, value in obj1.items():
        if i in newObj:
            newObj[i] += value
        else:
            newObj[i] = value

    for i, value in obj2.items():
        if i in newObj:
            newObj[i] += value
        else:
            newObj[i] = value
    return newObj

result = adding_objects({'a': 200, 'b': 50}, {'a': 100, 'c': 500})
print(result)
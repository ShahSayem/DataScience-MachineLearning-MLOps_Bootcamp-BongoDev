dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

for key in dict1:
    if key in dict2:
        print(f"Key: {key}, Value from dict1: {dict1[key]}, Value from dict2: {dict2[key]}")
    else:
        print(f"Key: {key}, Value from dict1: {dict1[key]}, Value from dict2: Not found!!!")

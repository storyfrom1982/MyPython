dic = {'name': 'liyongKang', 'age': 16}
print(dic)
print(dic['name'])
print(dic['age'])

dic['money'] = 1234567890
print(dic)
print(dic['money'])

dic['age'] = 46
print(dic)

del dic['age']
print(dic)

print(dic.get('age', 46))


for key, val in dic.items():
    print(f"key={key} val={val}")

for key in dic.keys():
    print(f'key={key}')

for key in dic:
    print(f"key={key}")

if 'age' not in dic.keys():
    dic['age'] = 46
    print(dic)

for key in sorted(dic.keys()):
    print(key)

for val in dic.values():
    print(val)

for val in set(dic.values()):
    print(val)

list_dict = [dic, dic, dic]
print(list_dict)

dic = {}
dic['fist'] = list_dict
dic['second'] = list_dict
print(dic)

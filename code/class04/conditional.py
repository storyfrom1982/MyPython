language = ['C', 'Python', 'Java', 'Rust', 'javascript']

for index, item in enumerate(language):
    if item == 'C':
        print(f"index {index}", item)
    else:
        print(f"index {index}", item.lower())


str = "str"
print(str == "str")
print(str != "str")

num = 10
print(str == 'str' and num == 10)
print(str == 'str' and num != 10)
print(str == 'str' and num < 20)
print(str == 'str' or num != 10)
    
print('C' in language)
print('C++' in language)
print('C++' not in language)
tmp = 'Java'
print(tmp not in language)
cond = True
print(tmp not in language or cond)

if tmp not in language:
    print('if')
elif not cond:
    print('elif')
else:
    print("else")

empty = []
if empty:
    print("list not empty")
else:
    print("list empty")
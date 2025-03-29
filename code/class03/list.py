# 创建列表
lang = ['C', 'Python', 'JS']
print(lang)

# 访问列表中的元素
print(lang[0])
print(lang[1])
print(lang[2])
print(lang[2].lower())
print(lang[-1].title())
print(lang[-2])

message = f"I love {lang[0]} and {lang[1]}!"
print(message)

# 修改列表中的元素
lang[-1] = "type script"
print(lang)
print(lang[-1].title())

# 在列表中添加元素
lang.append('Rust')
print(lang)
print(lang[-1])

lang.insert(2, 'Java')
print(lang)
print(lang[2])

# 删除列表中的元素
del lang[2]
print(lang)

lang.remove('Rust')
print("删除值 Rust:", lang)
lang.remove(lang[-1])
print("删除末尾元素:", lang)

py = lang.pop()
print(lang)
print("弹出元素:", py)
c = lang.pop(0)
print(lang)
print("弹出[0]:", c)

# 列表排序
lang = ['C', 'Python', 'JS', 'Rust', 'Java']
print(sorted(lang))
lang.sort()
print(lang)
print(sorted(lang, reverse=True))
lang.reverse()
print(lang)
print(sorted(lang, reverse=False))

print(len(lang))

# 遍历列表
print("print lang:")
for item in lang:
    print(item)


numbers = list(range(0, 10))
print("print number:", numbers)
for val in numbers:
    print(val)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(lang[0:3])
print(lang[:4])
print(lang[2:])

# for (i = 0; i < 5; ++i)
for item in lang[0:5]:
    print(item)

new_lang = lang[:]
new_lang.append('go')
lang.append('shell')
print(new_lang)
print(lang)

new_lang = lang
new_lang.append('qml')
lang.append('yam')
print(new_lang)
print(lang)


# 元组
rect = (0, 0, 100, 200)
print(rect)
print(rect[0], rect[-1])

rect = (-1, -1, 20, 30)
print(rect)
print(rect[0], rect[-1])
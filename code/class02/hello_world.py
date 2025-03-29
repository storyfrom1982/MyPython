message = "Hello World!"
print(message)

message = "Python 我来了！"
print(message)

name = "liyong kang"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "liyong"
last_name = "kang"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello {full_name.title()}!")
name = f"\tHello {full_name.title()}!"
print(name)

name = " Im kly is coder "
# rstrip() 清除末尾的空格
rs_name = name.rstrip()
print(rs_name)
# lstrip() 清除开始的空格
ls_name = name.lstrip()
print(ls_name)

url = "https://www.baidu.com"
print(url.removeprefix("https://"))

suffix = "python_nodes.txt"
print(suffix.removesuffix(".txt"))

message = "test Python's diveres."
print(message)
message = 'test Python\'s diveres.'
print(message)

zhenli = "毛主席说：“实践是检验真理的唯一标准！”"
print(zhenli)
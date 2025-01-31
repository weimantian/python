
# 字典：包含键值对的数据
# my_info = {"name":"wmt", 'age':28, "gender":"man"}

# 创建一个空字典
my_info = {}

# 添加键和对应的值
my_info["name"] = "wmt"
my_info["age"] = 28
my_info["gender"] = "男"
my_info["weight"] = "72kg"

# 输出打印字典
print(f"my_info = {my_info}")

# 访问键值对：用[]来访问键的值时，若键不存在会报错
print(f"My name is {my_info['name']}")

# 访问键值对：用get()来访问，当访问的键不存在时，可以用第二个参数来返回一个异常
print(f"My age is {my_info.get('age')} years old")
print(f"My height is {my_info.get('height')} cm") # 键不存在时返回None
print(f"My score is {my_info.get('score', '不存在')}") # 键不存在时返回None


# 修改字典的值
my_info["age"] = 29
print(f"my_info = {my_info}")


# 删除键值对
del my_info["weight"]
print(f"my_info = {my_info}")

# 遍历字典 for key, value in my_info.items():
for key, value in my_info.items() :
	print(f"'{key}'': '{value}'")

print(my_info.items(), type(my_info.items()))


# 遍历字典所有的键 for key in my_info.key()
for key in my_info.keys():
	print(key)

print(my_info.keys(), type(my_info.keys()))

for key in my_info.values():
	print(key)

# 按照特定顺序来返回


























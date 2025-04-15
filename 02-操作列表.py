languages = ['C', 'C++', 'python', 'java', 'html']

# 遍历列表
for language in languages :
	print(language)

 # range()
print('range(5): ')
for value in range(5) :
 	print(value)

print('range(1, 5): ')
for value in range(1, 5) :
	print(value)
# 创建一个数值列表
digits = list(range(0, 10))
print(f"digits[] = {digits}")

# 对数字列表进行统计
print(f"min(digits) = {min(digits)}")
print(f"max(digits) = {max(digits)}")
print(f"sum(digits) = {sum(digits)}")

# 列表解析
squars = [value**2 for value in range(1,10)]
print(f"squars = [value**2 for value in range(1,10)] = {squars}")

# 列表切片
print(f"squars[0:3] = {squars[0:3]}")
print(f"squars[:3] = {squars[:3]}")
print(f"squars[3:] = {squars[3:]}")
print(f"squars[-3:] = {squars[-3:]}")

#访问列表的最后一个元素
print(f"squars[]的最后一个数据为{squars[-1]}")

# 列表复制
squars_copy = squars # 只是将squars_copy关联到squars列表
print("squars_copy = squars: ")
squars_copy.append(0)
print(f"squars = {squars}")
print(f"squars_copy = {squars_copy}")

squars_copy = squars[:] #
print("squars_copy = squars[:]: ")
squars_copy.append(0)
print(f"squars = {squars}")
print(f"squars_copy = {squars_copy}")

# 字符串切片
str_t = 'hello world'
print(str_t[0:2])

## 将字符列表以字符串形式输出

list = ['h', 'e', 'l', 'l', 'o']
ls = "".join(list)
print(ls)










# 列表
# 列表是一种有序的集合，可以随时添加和删除其中的数据
# 列表的声明
lst = []
print(lst)
# 创建一个包含数字1-5的列表
lst = [1, 2, 3, 4, 5]
print(lst)

# 创建一个包含数字1-9的列表
lst = list(range(1, 10))
print(lst)

# 创建一个包含偶数的列表
lst = [value for value in range(1, 10) if value % 2 == 0]
print(lst)

# 创建一个包含数字0-9的列表
lst = [0] * 10
print(lst)

# 将列表中的元素添加到列表末尾
lst = [1, 2, 3, 4, 5]
lst.extend([6, 7, 8])
print(lst)

# 将列表中的元素添加到列表末尾
lst.append([9, 10])
print(lst)

# 访问列表中的元素
ls = ['a'] 
print(ls[0]) # 访问列表的第一个数据

ls.append("hello")
print(ls, f"length: {len(ls)}")

message = f"{ls[1]} world!"
print(message)

ls.insert(2,"wa")
print(ls, f", length: {len(ls)}")

ls.insert(5, "haha")
print(ls, f", length: {len(ls)}") # 添加位置超出列表长度时，在末尾添加数据

del ls[0]
print(ls, f", length: {len(ls)}")

message = ls.pop()
print(f"弹出: '{message}'")
print(ls, f", length: {len(ls)}")

message = ls.pop(0)
print(f"弹出: '{message}'")
print(ls, f", length: {len(ls)}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
print(motorcycles, f", length: {len(motorcycles)}")
motorcycles.remove('yamaha')
print(motorcycles, f", length: {len(motorcycles)}")

print(f"临时排序：{sorted(motorcycles)}")
print(f"{motorcycles} , length: {len(motorcycles)}, 临时排序后原理列表没变化")

motorcycles.sort()
print(motorcycles, f", length: {len(motorcycles)}")

motorcycles.reverse()
print(motorcycles, f", length: {len(motorcycles)}")

# 将字符串转为列表
str_list = "Hello World"
print(list(str_list))








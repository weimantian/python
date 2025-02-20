print("hello")
# a = input("please input the words: ")
# print(a)

# 列表
# append()：在列表末尾添加数据
# insert(位置, 数据)：在指定位置添加数据
# del 语句：删除指定位置的元素，例如：del list[1],删除索引位置为1的数据
# pop(): 参数为空时删除末尾的数据，并返回末尾数据，类似出栈；参数不为空时弹出指定位置的数据
# remove(要删除的数据): 根据值删除数据，只能删除第一个数据
# sort(): 列表永久排序
# sorted(); 列表临时排序
# reverse()：永久反转列表
# len(ls): 计算列表长度
ls = [] # 空列表
ls.append([1,2]) # 在末尾添加数据
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










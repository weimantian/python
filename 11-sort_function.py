# sort()：永久排序

# 典型用法示例
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # 对列表进行升序排序
print("Sorted list:", numbers)

# 双重排序示例
items = [(3, 2), (1, 4), (3, 1), (2, 2), (1, 3)]
items.sort(key=lambda x: (x[0], x[1]))  # 首先按第一个元素排序，然后按第二个元素排序
print("Doubly sorted list:", items)

# 逆序双重排序示例
items.sort(key=lambda x: (x[0], x[1]), reverse=True)  # 按照双重排序结果的逆序排列
print("Doubly sorted list in reverse order:", items)

# 定义一个类
class Item:
    def __init__(self, primary, secondary):
        self.primary = primary  # 主要排序键
        self.secondary = secondary  # 次要排序键

    def __repr__(self):
        return f"Item({self.primary}, {self.secondary})"  # 返回对象的字符串表示

# 创建类的实例列表
item_objects = [Item(3, 2), Item(1, 4), Item(3, 1), Item(2, 2), Item(1, 3)]

# 双重排序类的实例
item_objects.sort(key=lambda x: (x.primary, x.secondary))  # 按照primary和secondary属性排序
print("Doubly sorted list of objects:", item_objects)

# 逆序双重排序类的实例
item_objects.sort(key=lambda x: (x.primary, x.secondary), reverse=True)  # 按照排序结果的逆序排列
print("Doubly sorted list of objects in reverse order:", item_objects)
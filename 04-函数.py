# 定义函数 def fun(parm) : 
def  describe_animal(animal_name, pet_name) :
	print(f"I have a {animal_name}.")
	print(f"My {animal_name}'s name is {pet_name}")

describe_animal('dog', '旺财')
print()

# 关键字实参,防止参数传递错误
describe_animal(animal_name='cat', pet_name='pupu')
print()

# 默认值
def  describe_animal(animal_name, pet_name='来福') :
	print(f"I have a {animal_name}.")
	print(f"My {animal_name}'s name is {pet_name}")

describe_animal('dog')
print()

# 函数返回值
# title()函数，将首字母大写
def get_formatted_name(frist_name, last_name):
	full_name = f"{frist_name} {last_name}"
	return full_name.title()
print(get_formatted_name('jim', 'hendrix'), '\n')

# 函数参数为列列表时，函数可永久修改参数列表的值
# 打印设计，并将已经打印的设计做好统计
def print_name(unprinted_designs, completed_designs):
	"""
	1.模拟打印，直到将所有设计打印
	2.将已经打印的模块统计到已完成打印的列表中
	"""
	while(unprinted_designs):
		current_design = unprinted_designs.pop();
		print(f"正在打印 {current_design} ...")
		completed_designs.append(current_design)
		print(f"{completed_designs} 已完成打印")
		print(f"{unprinted_designs} 未打印\n")



designs = ["car", "cat", "table", "book"]
completed_designs = []
print_name(designs, completed_designs)
print(designs)

# 禁止修改参数列表的值：调用函数时列表参数使用切片
def print_name(unprinted_designs, completed_designs):
	"""
	1.模拟打印，直到将所有设计打印
	2.将已经打印的模块统计到已完成打印的列表中
	"""
	while(unprinted_designs):
		current_design = unprinted_designs.pop();
		print(f"正在打印 {current_design} ...")
		completed_designs.append(current_design)
		print(f"{completed_designs} 已完成打印")
		print(f"{unprinted_designs} 未打印\n")



designs = ["car", "cat", "table", "book"]
completed_designs = []
print_name(designs[:], completed_designs)
print(designs)
print()


# 传递任意数量的实参
# 制作披萨函数：make_pizze(*toppings),参数*toppings的*号是让函数创建一个toppings的空元组
def make_pizza(size, *toppings):
	print(f"Makeing a pizzze size of {size}, with flloweing toppings: ")
	for topping in toppings:
		print(f"- {topping}")


make_pizza("12英寸", "香肠", "土豆", "番茄")










# 创建 Dog 类，每个Dog有name和age，并且有蹲下sit()和打滚roll_over()的能力

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting...")

	def roll_over(self):
		print(f"{self.name} is rolled over!\n")

	def set_age(self, new_age):
		self.age = new_age

# 创建实例
my_dog = Dog("来福", 2)

# 访问实例属性
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.\n")

# 调用实例方法
my_dog.sit()
my_dog.roll_over()

# 修改实例属性
# 1.直接修改属性值
my_dog.name = "旺财"
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.\n")

# 2.通过方法修改属性值
my_dog.set_age(3)
print(f"my dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.\n")


# 继承
class Dog_1(Dog):
	def __init__(self, name, age):
		super().__init__(name, age) # super让Dog_1能调用父类的方法
		self.color = "withe" # 给子类定义特有的属性

	# 重新定义父类的方法
	def set_age(self):
		print("haha\n")

my_dog_1 = Dog_1("pupu",4)
print(f"my dog's name is {my_dog_1.name}.")
print(f"my dog is {my_dog_1.age} years old.")
print(f"my dog's color is {my_dog_1.color}.")
my_dog_1.sit()
my_dog_1.roll_over()
my_dog_1.set_age()













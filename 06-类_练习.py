
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type, number_served=0): # cuisine 饭菜
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	def describe_restaurant(self):
		print(f"饭店名称 : {self.restaurant_name}, 饭菜类型 : {self.cuisine_type}")

	def open_restaurant(self):
		print("营业中")

	def print_number_served(self):
		print(f"有{self.number_served}人在此饭店就餐过")

	def set_number_servesd(self, number_served):
		self.number_served = number_served

	def increment_number_served(self, increment_number_served):
		self.number_served += increment_number_served



my_restaurant = Restaurant("重庆鸡公煲", "中餐")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.print_number_served()
my_restaurant.set_number_servesd(10)
my_restaurant.print_number_served()
my_restaurant.increment_number_served(12)
my_restaurant.print_number_served()

print()

class User:
	def __init__(self, frist_name, last_name, gender, login_attempts=0):
		self.frist_name = frist_name
		self.last_name = last_name
		self.gender = gender
		self.login_attempts = login_attempts

	def describe_name(self):
		print(f"first_name : {self.frist_name}, last_name : {self.last_name}")

	def greet_user(self):
		if(self.gender == "女"):
			print(f"你好{self.frist_name}小姐")
		else:
			print(f"你好{self.frist_name}先生")
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(f"{self.frist_name}尝试登陆次数：{self.login_attempts}")


	def resert_login_attempts(self):
		self.login_attempts = 0
		print(f"{self.frist_name}尝试登陆次数：{self.login_attempts}")

user_00 = User("魏", "曼天", "男")

user_00.describe_name()
user_00.greet_user()
user_00.increment_login_attempts()
user_00.increment_login_attempts()
user_00.increment_login_attempts()
user_00.increment_login_attempts()
user_00.resert_login_attempts()








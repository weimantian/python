import json
"""
username = input("What is you name?")

file_name = "username.json"

with open(file_name, 'w') as file_object:
	json.dump(username, file_object) # 将数据写入到json文件中

with open(file_name) as file_object:
	data = json.load(file_object)

print(f"username: {data}, type: {type(data)}")
"""
def get_username():
	file_name = "username.json"
	try:
	 	with open(file_name) as file_object:
	 		username = json.load(file_object)
	except FileNotFoundError:
	 	return None
	else:
		return username

def greet_user():
	username = get_username()
	if username:
		print(f"hello {username}")
	else:
		username = get_new_username()
		print(f"I will remember you when you come bace, {username}")

def get_new_username():

	username = input("What is you name?")
	file_name = "username.json"
	with open(file_name, 'w') as file_object:
		json.dump(username, file_object) # 将数据写入到json文件中
	return username

greet_user()
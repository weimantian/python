 # 读取demo.txt文件内容
with open('demo.txt') as file_object: # 读取demo.txt的内容并赋值给file_object对象
	
	# for value in file_object: # 逐行读取文件内容
	# 	print(f"value: {value.rstrip()}")
	# print(file_object.mode)
	contents = file_object.read() # 读取file_object文件对象的全部内容
	print(f"contents type: {type(contents)}")
	# print(file_object.mode)


print(f"contents: {contents}") 


def write_pi(contents, file_nmae):
	with open(file_nmae,"w") as file_object:
		file_object.write(contents)

write_pi(contents, "demo_wirte.txt")




# rstirp([param])删除末尾多余的指定字符，参数为空时删除空格
# strip([param])删除头尾对于的指定字符，参数为空时删除空格

str_test = "   hello ssss    ss   "
print(f"原字符串: {str_test}, 长度: {len(str_test)}")
new_str = str_test.rstrip() # 去除末尾空格
print(f"str_tst.rstrip(): {new_str}, 长度: {len(new_str)}")
new_str =new_str.rstrip("s") # 去除末尾s
print(f"str_tst.rstrip('s'): {new_str}, 长度: {len(new_str)}")
print(f"原字符串: {str_test}, 长度: {len(str_test)}")
print(f"str_test.strip(): {str_test.strip()}")

str = "sshhhss"
print(str.strip("s"))
print(str.rstrip("s"))
# 字符串分割
str_list = "Hello World".split()
print(str_list)

str_list = "Hello World".split("o")
print(str_list)



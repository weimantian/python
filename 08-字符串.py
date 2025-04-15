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

# Return the Unicode code point for a one-character string.
# ord(c: str | bytes | bytearray, /) -> int)
print(ord("b"))

##  访问最后一个元素
string = "hello world!"
print(string[-1])
## 字符串分割 str.split(sep=None, maxsplit=-1)：返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。
print(string.split('o'))  # ["hell", "o", " w", "o", "rld"]
print(string)

s = "ssstrrtgdfssffss"
# str.lstrip([chars])
# 返回原字符串的副本，移除其中的头部字符
print(s.lstrip("ss"))
# str.rstrip([chars])
# 返回原字符串的副本，移除其中的末尾字符
print(s.rstrip("ss"))
# str.strip([chars])
# 返回原字符串的副本，移除其中的头部和末尾字符
print(s.strip("ss"))



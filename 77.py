'''
读文件过程：
1、打开文件
2、读取文件内容
3、关闭文件

'''
'''
1、打开文件
open(path,flag[, encoding][, errors])
path:要打开文件的路径
flag:打开文件的方式
r:以只读的方式打开文件，文件的描述符放在文件的开头
rb：以二进制格式打开文件，用于只读，文件的描述符放在文件的开头
r+：打开一个文件用于读写，文件的描述符放在文件的开头
w：以只写方式打开一个文件，如果该文件已经存在，会覆盖以前的内容，如果不存在，则创建一个文件
wb：打开一个文件用于写入二进制，如果该文件已经存在，会覆盖以前的内容，如果不存在，则创建一个文件
w+：打开一个文件用于读写，如果该文件已经存在，会覆盖以前的内容，如果不存在，则创建一个文件
a：打开一个文件，用于追加，如果文件存在，文件描述符将会放到文件末尾
a+：打开一个文件
encoding:编码方式
errors:错误处理



'''
import time

path = r"C:\Users\lz\Desktop\github\CX.PY\文件读写\file1.txt"
# ingore  忽略错误
# f = open(path, "r", encoding="UTF-8", errors="ignore")
f = open(path, "r")
'''
2、读文件内容
'''
# 1、读取文件的全部内容
# str1 = f.read()
# print(str1)

# 2、读取指定字符数
# str2 = f.read(10)
# print(str2)
# str3 = f.read(10)
# print("str3:" + str3)
# print("*" + str3 + "*")

# 3、读取整行，包括\n字符
# str4 = f.readline()
# print('str4:' + str4)

# 4、读取指定字符数
# str6 = f.readline(20)
# print("str6:" + str6)


# 5、读取所有行并返回一个列表
# list7 = f.readlines()
# print("str7")
# print(list7)


# 6、若给定的数字大于0，返回实际size字节的行数
list8 = f.readlines(20)
print('str8')
print(list8)

# 修改文件描述符的位置
print("***8")
f.seek(0)
str9 = f.read()
print('str9')
print(str9)

'''
3、关闭文件
'''
f.close()

# 一个完整的过程
try:
    f1 = open(path, "r")
    print(f1.read())
finally:
    if f1:
        f1.close()

# 最简单的方式，with可以自动把文件关上
with open(path, "r") as f2:
    print(f2.read())

#  写文件
print('-----------------------')
path = r"C:\Users\lz\Desktop\github\CX.PY\文件读写\file2.txt"
f = open(path, "w")
# 开始写
# 1.将信息写入缓冲区
f.write("i am a good man1")

# 2、刷新缓冲区
# 直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入
f.flush()

while 1:
    f.write("i am a good man!")
    f.flush()
    time.sleep(0.01)

f.close()
with open(path, "a") as f2:
    f2.write("good man")




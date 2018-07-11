#!/usr/bin/python
import sys
<<<<<<< HEAD

=======
print("我是分支2次修改")
>>>>>>> new1
print("我是分支修改")

i = 10
print(i)
m = 11
str = "你好，时间"
print(m)
print("你好")

print('the third time')
print(str)
if True:
    print("ansuer")
else:
    print("no")
print("myname")
#raw_input("按下enter键退出，其他任意键显示...\n")

list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(list)
print(list[1:3])
print(list[1:])

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(tinydict)
print(tinydict.keys())
print(tinydict.values())

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a),type(b),type(c),type(d))

print ("我叫 %s 今年 %d 岁!%d" %('小明',12,10))

str1='www.baidu.com'
aa=str1.center(40,'*')
print(aa)

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))

str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))
print ("str.zfill : ",str.zfill(30))

list1 = ['a','g','x']
print(max(list1))
print(list1.index('x'))


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]

# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(reverse=True,key=takeSecond)

# 输出类别
print('排序列表：', random)

random.sort()
print(random)

random.sort(reverse=True)
print(random)

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)

print(dict2.keys())
print(dict2.values())



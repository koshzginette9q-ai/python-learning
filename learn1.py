#一个Tap为缩进
#字符串
str_v="a real man"
print(str_v)
#数字
num_v=9178
#bool
bool_v=True#首字母大写
#集合
set_v={1,2,3,1}
#元组
tuple_v=(1,2,3)
#列表
list_v=[1,2,3]
#字典
dict_v={'a':1,'b':2,'c':3}
print(dict_v)
#print 函数的原理是输出仅一个单独的变量
str0='A real man,he knows what he needs to do'
print(str0)
#想在字符串中插入其它变量，可使用“f 字符串”的方法
str1="money path"
str2="doctor"
str3 =f"you ruined his {str1}.you ruined his {str2}"
print(str3)
answer=0.98
print(f"测试集的准确率为{answer}")
#字符串中添加转义字符，如换行符\n 与制表符\t
message="shop sells:\n\tlitchi\n\tfritters\n\tfried fish"
print(message)
'''+加-减*乘/除 **幂
//取整%取余'''
#bool
# 集合——检查某变量是否在该集合中，元组，列表，字典同理
print(2 in set_v)
#字符的转换
print(float(num_v))
#元组
print(1,2,3,4,5)
# 元组法替代 f 字符串
print('最终成绩:',answer)
# 元组拆分法——极速创建新变量
a,b,c=1,2,3
print(c,b,a)
# 元组拆分法——极速交换变量值
(a,b,c)=(c,b,a)
print(a,b,c)
# 元组拆分法——只要前两个答案
values=(12,13,14,15,16,17,18)
a,b,*rest=values
print(a,b,rest)

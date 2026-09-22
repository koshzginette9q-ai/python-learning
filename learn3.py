#循环语句
#for 循环遍历列表
Food=['米','面','馄饨']
for i in Food:
    message=f"{i},yummy"
    print(message)
print('I love them all')
#for 循环遍历字典
person={'zss':'best friend','lkw':'girlfriend'}
for k in person.keys():
    print('person_name:',k)
for v in person.values():
    print('relationship:',v)
for k,v in person.items():
    print(k,'is my',v)
#while 循环
#continue 与 break
a=1
while a<=5:
    print(a)
    if a==3:
        break
    a+=1
a=0
while a<5:
    a+=1
    if a==3:
        continue
    print(a)
#高级变量间的转换,以字典为例
set_v={1,2,3}
tuple_v=(1,2,3)
list_v=[1,2,3]
dict_v={'a':1,'b':2,'c':3}
print(dict(zip(['a','b','c'],set_v)))
print(list(set_v))




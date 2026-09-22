#列表
#列表可以容纳各种变量类型，其代价是——列表要单独存储,每一个元素的变量类型，列表越大越占空间
list1=['cxk',1,True,{1,2},(1,2),[1,2],{'a':1,'b':2}]
print(list1)
#访问与修改某个元素
print(list1[0],list1[5])
#访问列表倒数第一个元素时，可使用 a[-1]
print(list1[-1])
list1[1]=9178
print(list1)
#切片——访问部分元素
list2=['a','b','c','d','e']
print(list2[:2])
print(list2[2:])
print(list2[1:-2])
#明确隔几个元素采样一次
print(list2[::2])# 每 2 个元素采样一次
print(list2[1:-1:2])# 切除一头一尾后，每 2 个元素采样一次
#切片不影响视图
cut2=list2[:2]
cut2[1]='q'
print(cut2,list2)
#列表元素的添加 列表可以使用 + 和 * 来添加原列表
list3=[1,2,3]
print(list3+[4,5])
print(list3*2)
#字典,理解为升级的列表
dict1={'a':1,'b':2,'c':3}
print(list3[1],dict1['b'])
#字典元素的修改、添加与删除
ZZU={'食堂':'夯',
     '宿舍':'拉'}
# 添加元素
ZZU['校园']='夯'
print(ZZU)
# 添加元素
del ZZU['宿舍']
print(ZZU)


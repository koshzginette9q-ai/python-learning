#函数
def my_func(v):
    '''这是用来注释的，这个函数没有函数体'''
    return v
str_v=my_func('jee')
print(str_v)
# 吞吐多个变量 输入多个值本质是输入了一个元组，输出多个值本质是输出了一个元组
def his_hobbies(name,*hobbies):
    return name,hobbies
n,h=his_hobbies('cxk','singing','dancing','rap','basketball')
print(f"{n}likes{h}")
#吞吐多个普通参数，并附带一个任意数量的键值对参数
def evaluate1(in1,in2,**kwargs):
    kwargs['计算机类']=in1
    kwargs['通信工程']=in2
    return kwargs
eva1=evaluate1('敲代码的','拉网线的')
print(eva1)
eva2=evaluate1('敲代码的','拉网线的',电子工程='焊电路的')
print(eva2)
#输入参数的默认值
def evaluate2(in1='敲代码的',in2='拉网线的',**kwargs):
    kwargs['计算机类']=in1
    kwargs['通信工程']=in2
    return kwargs
#函数的关键字调用
eva2=evaluate1(in2='拉网线的',in1='敲代码的')
print(eva2)

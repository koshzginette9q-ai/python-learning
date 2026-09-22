#类
#创建和使用类（包含默认值）
class Counter:
    def __init__(self,a,b):
        ''' a 和 b 公共变量，也是 self 的属性'''
        self.a=a
        self.b=b
        self.c=5
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
cnt=Counter(5,6)
print(cnt.a,cnt.b)
print(cnt.add())
cnt.c=9178
print(cnt.c)
# 继承
class Counter2(Counter):
    def __init__(self,a,b):
        '''引用父类属性'''
        super().__init__(a,b)
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
test1=Counter2(1,2)
print(test1.c,test1.div())
#掠夺
class Amrc:
    def __init__(self,c,d):
        self.c=c
        self.d=d
        self.cnt=Counter(c,d)
    def mul(self):
        return self.c*self.d
test2=Amrc(1,2)
print(test2.mul(),test2.cnt.add())
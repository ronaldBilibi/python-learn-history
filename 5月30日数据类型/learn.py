#这个就是e科学计数法，小数点后16位数 ，直接为 2.5-e151
ronald = 0.0000000000000025
print(ronald)
#太阳距离地球的距离是 1.5亿千米 ，也就是15后10个零
realsun = 150000000000
print('sun',realsun)
#这样写很麻烦 so
nicesun = 1.5e11
print('nicesun',nicesun)
#sum e计算是浮点类型
if 15000 == 1.5e4:
    print('15000=1.5e4')
#布尔类型相当于整数型
if True == 1:
    print('True==1')
if False == 0:
    print('False==0')
#类型转换；note 只能转换纯数字如果里面有中文或英文则不行
a = '666'
print(type(a),'now type of a  is str')
a = int(a)
print(type(a),'now a is int')
#浮点型转换成整型，会地板算法去掉小数点后的直接保留整数位
a=6.99
b=int(a)
print('b',b)
#关于数字类型
type(5)
type('5')
type('5.1')
type('5e15')
#不够yhon建勇用
a='小青玩'
print(isinstance(a,str))
print(isinstance(a,int))


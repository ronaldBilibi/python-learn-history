while True:
    
    x=int(input('请输入x数值'))
    y = int(input('请输入y数值'))
    small = x if x<y else y
    print(small)
#如果 x<y 为真， 则x 赋值与small ，否则y

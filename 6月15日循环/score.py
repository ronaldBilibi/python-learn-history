while True:
    score = int(input("请输入分数"))
  
    if isinstance(score,int):
        if score >= 90 and score <=100:
            print('A')
        elif score >=80 and score <90:
            print('B')
        elif score >=60 and score <80:
            print('c')
        elif score >=0 and score < 60:
            print('D')
        else:
            print("张迪爱学习")
    else:
        score = input('请输入整数分') 
            

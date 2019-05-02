import random   #random() 方法返回随机生成的一个实数，它在[0,1)范围内。
# random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
num = random.randint(1,10)  # 产生 1 到 10 的一个整数型随机数
count = 0
while(count<5):   #传入猜的次数
    input_num = input('please input num that you guess:')
    try:
      input_num = int(input_num)  #int() 函数用于将一个字符串或数字转换为整型。把你猜的值转成整数
      if input_num == num:
         print('bingo，luck you')
      elif input_num < num:
         print('猜小了')
      else:
         print('猜大了')
    except ValueError:   # ValueError 传入无效的参数
        print('请输入数字')
    count += 1

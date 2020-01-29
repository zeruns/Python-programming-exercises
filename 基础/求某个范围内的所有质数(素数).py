#质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。

#方法1
def primeNUM(min,max):
    if min==1:
        print('')
        min += 1
    for i in range(min, max+1):
        for j in range(2, i + 1):
            if i % j == 0:          #判断i能不能被整除
                break               #退出for循环
        if j == i:                  #若j等于i，说明i是素数
            print(i,end=" ")
    print('')
primeNUM(1,200)

#方法2
def test(num):
    list = []              #定义一个列表 用于存储计算的数
    i = num -1             # 去除本身
    while i > 1:           # 去除1
        if num %i == 0 :   #判断是否有余数
            list.append(i) # 将所有的能整除i的数加入列表
        i -= 1
    if len(list) == 0 and num != 1:     # 如果列表为空 就是表示除了1和它本身能整除
        print(num,end=' ')

def primeNUM2(min,max):
    j = min
    while j < max:
        test(j)
        j += 1
    print('')
primeNUM2(1,100)
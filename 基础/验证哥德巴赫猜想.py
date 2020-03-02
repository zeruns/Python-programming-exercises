'''
1742年6月，德国著名的数学家哥德巴赫(C.Goldbah 1690-1764)预言：
**“任何一个6以上的偶数都可以分解为两个素数的和“**
这就是著名的哥德巴赫猜想，俗称“1+1= 2“，例如
6=3+3
8=5+3
10=5+5
一个偶数分解成两个素数的和的分解不是唯一的，例如
24=5+19
24=17+7
'''


def ss(i):  # 判断一个数是否素数
    j = 0
    for j in range(2, i + 1):
        if i % j == 0:
            break
    if j == i:  # 当j等于i时说明循环没有被中断，i不能被除1和它本身之外的数整除，i是素数
        return 1  # 如果是素数就返回1
    else:
        return 0  # 如果不是素数就返回0


# 验证某个范围内的数
flag = 1
for n in [a for a in range(4, 8888) if a % 2 == 0]:  # 生成4到8888之间的偶数
    maxp = n / 2
    for p in range(int(maxp), 0, -1):
        if ss(p):  # 判断p是否素数
            q = n - p
            if ss(q):  # 判断q是否素数
                print('%d = %d + %d    OK!' % (n, p, q))  # p和q都为素数时说明n符合哥德巴赫猜想
                break  # 跳出循环继续下一个数的验证
            elif p == 1:  # 当p等于1时说明n不符合哥德巴赫猜想
                print(n, '   NO!')
                flag = 0
    if flag == 0:
        break

# 一直验证到失败为止
flag = 1
n = 4
while flag == 1:
    maxp = n / 2
    for p in range(int(maxp), 0, -1):
        if ss(p):
            q = n - p
            if ss(q):
                print('%d = %d + %d    OK!' % (n, p, q))
                break
            elif p == 1:
                print(n, '   NO!')
                flag = 0
    n += 2

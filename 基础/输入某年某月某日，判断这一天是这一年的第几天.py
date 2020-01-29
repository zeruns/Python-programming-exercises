# 用函数实现输入某年某月某日，判断这一天是这一年的第几天，闰年情况也考虑进去

month31 = [1, 3, 5, 7, 8, 10, 12]  # 一个月有31天的月份
month30 = [4, 6, 9, 11]  # 一个月有30天的月份


def leap_year(year):  # 判断闰年，如果是闰年就返回1，不是就返回0
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  # 判断条件：能被400整除的年份 或者 能被4整除，但是不能被100整除的年份
        return 1
    else:
        return 0


def shuru():  # 获取用户输入
    i = 1
    while i == 1:
        time = input("请输入年月日(以/为分隔符，例如2020/01/30)：")  # 将输入的字符串放入time变量中
        time2 = time.split('/')  # 将time字符串以"/"为分隔符进行分隔，将分隔后的字符串放入列表time2中
        year = int(time2[0])  # 将列表time2中下标为0的字符串转为整数类型放入变量year中
        month = int(time2[1])
        day = int(time2[2])
        if len(time2) == 3 and (
                (month in month31 and day in range(1, 32)) or (month in month30 and day in range(1, 31)) or (
                month == 2 and day in range(1, 30) and leap_year(year)) or (
                        month == 2 and day in range(1, 29) and leap_year(
                    year) == 0)):  # 判断输入的年月日是否符合规范，如果符合规范就使i等于0使循环结束，否则就打印“输入错误”然后继续重新输入
            i = 0
        else:
            print('输入错误')
    year = int(time2[0])
    month = int(time2[1])
    day = int(time2[2])
    return year, month, day, time


def js(year, month, day, time):  # 计算第几天
    day_sum = 0
    for x in range(1, month + 1):
        if x in month31 and month > 1:
            day_sum += 31
        elif x in month30 and month > 1:
            day_sum += 30
        elif x == 2 and leap_year(year) and month > 2:
            day_sum += 29
        elif x == 2 and month > 2:
            day_sum += 28
    day_sum += day
    print("%s是%d年的第%d天" % (time, year, day_sum))


year, month, day, time = shuru()
js(year, month, day, time)

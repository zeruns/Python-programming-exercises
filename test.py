def leapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("%d是闰年"%year)
    else:
        print("%d不是闰年"%year)

leapyear(int(input("请输入年份：")))
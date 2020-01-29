'''
用函数实现一个判断用户输入的年份是否是闰年的程序
1.能被400整除的年份
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年
'''

def leapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("%d是闰年"%year)
    else:
        print("%d不是闰年"%year)

leapyear(int(input("请输入年份：")))
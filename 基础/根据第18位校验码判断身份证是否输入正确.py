ID = input("请输入身份证号码：")
W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
sum = 0
for i in range(17):
    sum = sum + int(ID[i]) * W[i]
if Checkcode[sum % 11] == int(ID[17]):
    print('输入正确')
else:
    print('输入错误')

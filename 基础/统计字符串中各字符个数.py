'''
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''

a="hello world"
b=[]
for i in a.replace(" ",""):
    if i in b:
        pass
    else:
        b.append(i)
for i in b:
    print("%s:%s"%(i,a.count(i)))
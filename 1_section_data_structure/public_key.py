#-*- coding: UTF-8 -*-
#如何找到多个字典中的公共键
from random import randint,sample
if __name__=='__main__':
    a1=sample('abcdefg',3)#随机采样3个
    print 1,a1
    a2=sample('abcdefg',randint(3,6))
    print 2,a2
    s1={x: randint(1,4) for x in sample('abcdef',randint(3,6))}
    s2 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
    s3 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}
    #使用集合操作，然后取交集，
    print 3,s1.viewkeys(),s2.viewkeys(),s3.viewkeys()
    print 4,s1.viewkeys()&s2.viewkeys()
    print 5,s1.viewkeys()&s2.viewkeys()&s3.viewkeys()
    #对于N 轮 map和reduce函数
    print  6,map(dict.viewkeys,[s1,s2,s3])
    print 7,reduce(lambda a,b:a&b,map(dict.viewkeys,[s1,s2,s3]))
    #reduce 对map的函数进行迭代法。

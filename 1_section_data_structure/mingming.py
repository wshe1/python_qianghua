#-*- coding: UTF-8 -*-
#如何为元组每个元素命名，提高程序的可读性，元组的速度何况快
from collections import namedtuple
from collections import Counter#计数器
from random import randint
import re
Name=0
AGE=1
SEX=2
EMAIL=3

if __name__=='__main__':
    student=('jim',16,'male','jim802@qq.com')
    print 1,student[Name],student[AGE],student[SEX],student[EMAIL]
    Student=namedtuple('Student',['name','age','sex','email'])
    s=Student('jimq',18,'male','jim802@qq.com')
    print 2,s.name,s.age,isinstance(s,tuple)
    #如何统计序列元素中出现的频度
    data=[randint(0,20) for _ in xrange(30)]
    print 3,data
    c=dict.fromkeys(data,0)
    for x in data:
        c[x]+=1;
    print 4,c
    c2=Counter(data)
    print 5,c2.most_common(3)#出现频度最高的3个
    #英文文章统计
    txt=open('english.txt').read()
    print txt
    #使用正则表达式的分割模块，进行单词分割
    c3=Counter(re.split('\W+',txt))
    print 7,c3.most_common(10)
    #如何根据字典中值的大小，对字典的项进行排序
    d={x:randint(60,100) for x in 'xyzabc'}
    print 8,sorted(d)#对键进行排序，值没了
    #把字典变成元组(90,'x')('value','key')
    print 9,sorted(zip(d.itervalues(),d.iterkeys()))
    print 10,sorted(d.iteritems(),key=lambda x:x[1])#key是传入一个函数







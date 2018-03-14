#-*- coding: UTF-8 -*-
#如何进行反向迭代,和如何实现反向迭代
from itertools import islice
from random import randint
from itertools import chain
class Floatrang:
    def __init__(self,start,end,step=0.1):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):
        t=self.start
        while t<=self.end:
            yield t
            t+=self.step
    #以双下划线开头和结尾代表pyhton中特殊方法专用的标示
    def __reversed__(self):
        t=self.end
        while t>=self.start:
            yield t
            t-=self.step

if __name__=='__main__':
    L=[1,2,3,4,5]
    print 1,reversed(L)#得到一个反向的迭代器
    print 2,iter(L)#得到一个正向迭代器
    for x in reversed(L):
        print 3,x

    #正向迭代器
    for x in Floatrang(1.0,5.0,0.5):
        print 4,x
    #反向迭代器,reversed 实际调__reversed__函数。
    for x in reversed(Floatrang(1.0,5.0,0.5)):
        print 5,x

    #如何对迭代器进行切片操作：
    f=open('english.txt','r')
    lines=f.readline()#readline()函数将全部内容读到内存中
    f.seek(0)#使文件的指针回到开头
    for line in f:
        print line
    f.seek(0)
    print 6,islice(f,2,6)
    for x in islice(f,2,6):
        print 7,x
    f.seek(0)
    for x in islice(f,4):#一个词参数代表是末尾值
        print 8,x
    f.seek(0)
    for x in islice(f,5,None):#从5到末尾
        print 9,x

    l=range(20)
    t=iter(l)
    for x in islice(t,5,10):
        print 10,x

    for x in t:
        print 11, x

    #多个迭代对象
    math=[randint(60,100) for _ in xrange(40)]
    english=[randint(60,100) for _ in xrange(40)]
    chinese=[randint(60,100) for _ in xrange(40)]
    for i in xrange(len(math)):
       print chinese[i]+english[i]+math[i]
    #并行使用内置的函数zip函数，它能将迭代对象合并，每次迭代返回一个元组
    t=zip([1,2,3,4],('a','b','c','d'))
    print 12,t
    #列表的长度不一致，则取较短的一个
    t1 = zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'),[6,7,8])
    print 13, t1

    total=[]
    for c,m,e in zip(chinese,math,english):
        total.append(c+m+e)

    print 14,total

    #串行使用标准库中的itertools.chain,它将多个迭代对象链接
    e1=[randint(60, 100) for _ in xrange(40)]
    e2=[randint(60,100) for _ in xrange(40)]
    e3=[randint(60,100) for _ in xrange(40)]
    e4=[randint(60, 100) for _ in xrange(40)]
    cout=0
    for s in chain(e1,e2,e3,e4):
        if s>90:
            cout+=1;
    print 15,cout









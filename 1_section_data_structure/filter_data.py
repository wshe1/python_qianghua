#-*- coding: UTF-8 -*-
#如何在列表，字典，集合中根据字典条件s筛选数据
from random import randint
import timeit

if __name__=='__main__':
    global data
    data=[1,4,5,-2,-6,8,9]
    res=[]
    for x in data:
        if x>=0:
            res.append(x)
    print 1,res
    #通用的迭代法
    data1=[randint(-10,10) for _ in xrange(10)]# 生成10随机序列
    #xrange 和range用法相同，不同的是range 生成的是一个list对象，xrange 是一个生成器
    print 2,data1
    #使用过滤器
    #fliter :接受一个函数和一个序列，函数依次作用到每个元素，根据返回值是Ture和Flase来决定是否保留该元素
    print 3,filter(lambda x:x>=0,data1)
    #使用列表解析,，是python 迭代的一种，用于实现for,while功能，且速度较快
    print 4,[x for x in data1 if x>=0]
    #函数计时
    t=timeit.timeit('x=1')
    print 5,t
    t1=timeit.timeit('filter(lambda x: x >= 0, [1,4,5,-2,-6,8,9])',number=1)
    t11 = timeit.Timer('filter(lambda x: x >= 0, data)',setup="from __main__ import data").timeit(1)
    print 6,t1,t11
    t2=timeit.Timer('[x for x in data if x>=0]',setup="from __main__ import data").timeit(1)
    print 7,t2
    d={x:randint(60,100) for x in range(1,21)}
    print 8,d
    #字典的解析
    print 9, {k:v for k,v in d.iteritems() if v>80}
    #集合解析
    s=set(data)
    print 10,s
    print 11,{x for x in s if x%2==0}




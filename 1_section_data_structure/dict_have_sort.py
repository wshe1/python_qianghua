#-*- coding: UTF-8 -*-
#如何让字典有序
#使用collections 下的OrdereDict来代替原来的字典。
from collections import OrderedDict
from time import time
from random import randint
if __name__=='__main__':
    d=OrderedDict()
    d['jim']=(1,25)
    d['bob']=(2,35)
    d['leo']=(3,40)
    for k in d:
        print k

    d1=OrderedDict()
    players=list('ABCDFEGH')
    start =time()
    for i in xrange(8):
        raw_input()
        p=players.pop(randint(0,7-i))
        end=time()
        print i+1,p,end-start
        d1[p]=(i+1,end-start)
    print '-'*20
    for k in d1:
        print k,d1[k]

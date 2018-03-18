#-*- coding: UTF-8 -*-
#如何进行拆分含有多种分割符的字符串
#ps aux :查看系统当前进程
import re
def mysplit(s,ds):
    res=[s]
    for d in ds:
        t=[]
        map(lambda x:t.extend(x.split(d)),res)
        res=t
    #return res
    return [x for x in res if x]

if __name__=='__main__':
    s='wshe      3266  0.0  0.1  24336  5360 pts/4    Ss   16:28   0:00 bash'
    print 1,s.split()
    #方法1：连续使用str.split()方法，每次处理一种分割符号。
    #当连续两个分割符时，会出现空分割
    s1='ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
    res=s1.split(';')
    t = []
    map(lambda x: t.extend(x.split('|')),res)
    print 2,t
    res=t
    t=[]
    map(lambda x: t.extend(x.split(',')), res)
    print 3, t
    res = t
    t = []
    map(lambda x: t.extend(x.split('\t')), res)
    print 3, t
    #使用for循环
    #字符串是一个可迭代对象，用于for循环。
    print 4,mysplit(s1,';,|\t')
    #使用正则表达式re.split()方法，一次行拆分字符串
    print 5,re.split('[,;\t|]+',s1)


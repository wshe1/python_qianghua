#-*- coding: UTF-8 -*-
#如何在迭代器和可迭代对象，in面是一个吸迭代对象
from collections import Iterator,Iterable
import requests #安装第三方的request库

def getwather(city):
    r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)#中国天气网接口
    data=r.json()['data']['forecast'][0]
    return '%s :%s,%s '%(city,data['low'],data['high'])

class weatherIter(Iterator):
    def __init__(self,cites):
        self.cites=cites
        self.index=0

    def getwather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)  # 中国天气网接口
        data = r.json()['data']['forecast'][0]
        return '%s :%s,%s ' % (city, data['low'], data['high'])

    def next(self):
        if self.index==len(self.cites):
            raise StopIteration
        city=self.cites[self.index]
        self.index+=1
        return self.getwather(city)

class WeatherIterable(Iterable):
    def __init__(self,cites):
        self.cites=cites

    def __iter__(self):
        return weatherIter(self.cites)

if __name__=='__main__':
    l=[1,2,3,4]
    s='abcde'
    for x in l:
        print x
    #如果是可迭代对象，通过pyhon 的iter()方法得到一个迭代器对象
    print 1,iter(l)
    #列表和字符串是可迭代对象，__iter__是迭代协议的接口，在字符串中没有__iter__,但是有__getitem__方法
    #迭代器接口:next()
    #for 循环的工作机制是:先由iter(l)生成一个迭代器，接下来不停的调用next(),直到出现stopIteration的异常
    #获得天气
    print 1, getwather(u'北京')
    print 2, getwather(u'呼和浩特')

    #实现一个迭代器对象
    #步骤1：实现一个迭代器对象WeatherIterator,next方法每次返回一个城市的气温
    #步骤2：实现一个可迭代对象WeatherIterable,__iter__方法返回一个迭代器对象
    for x in WeatherIterable([u'北京',u'上海',u'广州',u'长春',u'大连',u'呼和浩特']):
        print x




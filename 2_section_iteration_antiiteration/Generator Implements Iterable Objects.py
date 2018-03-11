#-*- coding: UTF-8 -*-
#如何在生成器实现可迭代对象
def f():
    print 'in f().1'
    yield 1
    print 'in f().2'
    yield 2
    print 'in f().3'
    yield 3

class PrimeNumbers:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isprimenum(self,k):
        if k<2:
            return False
        for x in xrange(2,k):
            if k%x==0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start,self.end+1):
            if self.isprimenum(k):
                yield k




if __name__=='__main__':
    g=f()
    print 1,g.next()
    #生成器会保存程序的运行状态，当第一次调用时g.next时返回1,当第二次调用g.next时将从yield 1处后开始执行
    print 2,g.next()
    print 3,g.next()#next()是迭代器接口
    #print 4,g.next()#抛出胃停止异常，和迭代器是一致。生成器对象也是一个可迭代对象
    g1=f()
    for x in g1:#可以放到in后面
        print x
    g2=f()
    print 4,g2.__iter__() is g2#__inter__返回是自身
    #将该类的__iter__方法实现生成器函数，每次yield 返回一个素数。

    for x in PrimeNumbers(1,100):#直接调用了__iter__方法。返回是一个迭代器对象，for 中in返回一个迭代器对象
        print x
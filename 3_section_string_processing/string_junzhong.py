#-*- coding: UTF-8 -*-
#如何进行字符串对齐
#使用字符串的str.ljust(),str.rjust;str.center()进行左右对其
#使用format()方法，传递类似:'<20','>20','^20'完成

if __name__=='__main__':
    s='abc'
    print 1,s.ljust(20)
    print 2,s.ljust(20,'+')
    print 3,s.rjust(20)
    print 4,s.center(20)
    print 5, format(s,'>20')#>代表左对齐
    print 6,format(s,'<20')#<右对其
    print 7,format(s,'^20')#居中
    d={'DistCull':500.0,'SmallCull':0.04,'loDist':100.0,'trilinear':40}
    print 8,map(len,d.keys())
    w=max(map(len,d.keys()))
    for k in d:
        print k.ljust(w),':',d[k]
        

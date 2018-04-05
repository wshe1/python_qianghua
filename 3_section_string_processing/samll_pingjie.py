#-*- coding: UTF-8 -*-
#如何将多个小字符串拼接成一个大字符串。拼接一个UDP 包

if __name__=='__main__':
    s1='abcdef'
    s2='defge'
    pl=["<0112>","<32","<1024x768>","<60>","<1>","<100.0>","<500.0>"]
    s=''
    for p in pl:
        s+=p
        print s
    print 1,s
    #但是，浪费
    ss=''
    ss.join(pl)
    print 2,ss
    ss1=['anc',123,54,'xys']
    ss2=''

    ss2.join([str(x) for x in ss1])#使用列表解析
    print 4,ss2
    ss3=''
    ss3.join((str(x) for x in ss1))#生成器
    print 5,ss3
    #1.迭代列表，连续使用‘+’ 操作系统依次拼接每一个字符串
    #2,使用str.join()方法，更加快速的拼接列表中的所有字符串



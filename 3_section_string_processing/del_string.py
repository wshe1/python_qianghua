#-*- coding: UTF-8 -*-
#去掉不要的字符，
#strip(),lstrip(),rstrip()方法字符串两端字符
#删除固定字符，使用切片拼接
#replace()方法或正则表达式re.sub()删除任意位置字符
#translate() ,可以删除多种不同字符
import re
import string
if __name__=='__main__':
    s='     abc  123    '
    print 1,s.strip()#两端
    print 2,s.lstrip()#左
    print 3,s.rstrip()#右
    s1='+++123---'
    print 4,s1.strip('-+')#去掉+-
    s2='abc:123'
    print 5,s2[:3]+s2[4:]
    s3='\tabc\t123\txyz'
    print 6,s3.replace('\t','')
    s4='\tabc\t123\txyz\rqwe'
    print 7,re.sub('[\t\r]','',s4)
    s5='abc123456xyz'
    string.maketrans('abcxyz','xyzabc')#映射表，string.translate
    s6='abc\refg\n253\t'
    print 8,s6.translate(None,'\t\r\n')#
    #去掉音调
    u=u'ni\u03011 ha\u030co,chi\u0304 fa\u0300n'

    print 9,u.translate({0x0301:None})
    print 10,u.translate(dict.fromkeys([0x0301,0x030c,0x0304,0x0300]))



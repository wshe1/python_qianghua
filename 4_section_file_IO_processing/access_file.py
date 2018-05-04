#-*- coding: UTF-8 -*-
#如何读写文本文件
#python 2.x 写入文件前对unicode 编码，读入文件二进制字符串解码
#python 3.x open指定‘t'的文本格式，encoding 指定编码格式
if __name__=='__main__':
    s=u'您好'#pyhon 2 中的unicode
    print 1,s.encode('utf8')
    print 2,s.encode('gbk')
    f=open('py2.txt','w')
    f.write(s.encode('gbk'))
    f.close()
    f=open('py2.txt','r')
    t=f.read()
    print 3,t.decode('gbk')
    #b'abxde' python3 中的byte
    #'你好’    pyhon3 中的unicode
    #写
    #open('py3.txt','wt',encode='utf8')
    #f.write('你好！‘）
    #读
    #open('py3.txt','rt',encode='utf8')
    #f.read()
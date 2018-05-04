#-*- coding: UTF-8 -*-
#如何读写二进制文件
import struct
import  array
if __name__=='__main__':
    f=open('Dome.wav','rb')
    info=f.read(44)
    print 1 ,struct.unpack('h',info[22:24])#声道数
    print 2,struct.unpack('i',info[24:28])#采样率
    print 3, struct.unpack('h', info[34:36])  #编码宽度
    f.seek(0,2)#文件指针到末尾
    print 4,f.tell()#文件的 字节数
    n=(f.tell()-44)/2
    buf=array.array('h',(0 for _ in xrange(n)))
    f.close()
    f = open('Dome.wav', 'rb')
    f.seek(44)
    f.readinto(buf)
    print 5,buf[0]
    print 6,buf[500]
    for i in xrange(n):buf[i]/=8
    f2=open('Dome1.wav','wb')#写入二进制文件
    f2.write(info)
    buf.tofile(f2)
    f2.close()




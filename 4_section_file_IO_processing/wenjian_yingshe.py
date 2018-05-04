#-*- coding: UTF-8 -*-
#如何设置文件的缓冲
#将文件写入到硬件设备上去，使用系统调用，I/O操作时间长，为了减少I/O 次数，文件通常使用缓冲区，分为全缓冲，行缓冲，无缓冲
import mmap
if __name__=='__main__':
    f=open('dome.txt','w')#默认是4096（由于不是在命令行中，是直接运行完了
    f.write('abc')
    f.write('+'*4093)
    f.write('-')

    f=open('dome2.txt','w',buffering=2048)#设置缓冲区为2048
    f.write('+'*1024)
    f.write('+'*1023)
    f.write('-'*2)
    #行缓冲
    f=open('dome3.txt','w',buffering=1)
    f.write('abcd')
    f.write('1234')
    f.write('\n')#写入/n时写入
    #无缓冲
    f = open('dome4.txt', 'w', buffering=0)
    f.write('a')
    #如何将文件映射到内存
    #访问二进制文件时，希望把文件映射到内存中，可以随机访问
    #嵌入式设备，寄存器被编址，到内存中，通过映射，访问这些寄存器
    #多个进程映射到同一个文件，还能实现进程通信的目的
    #使用标准库中mmap模块的mmap()，函数，它需要打开文件描述符作为参数
    #dd if=/dev/zero of=demo.bin bs=1024 count=1024
    f=open('demo.bin','r+b')
    m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
    print m[0]
    m[4:8]='\xff'*4
    m = mmap.mmap(f.fileno(), mmap.PAGESIZE*8, access=mmap.ACCESS_WRITE,offset=mmap.PAGESIZE*4)
    m[:0x1000]='\xaa'*0x1000


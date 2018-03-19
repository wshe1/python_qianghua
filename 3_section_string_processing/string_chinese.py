#-*- coding: UTF-8 -*-
#判断字符传a是否以字符串b开头或结尾，案例搜索目录下指定文件
import os,stat
import re
if __name__=='__main__':
    #使用字符串的str.startswith()和str.endswith()方法。多个匹配时参数使用元组
    print 1,os.listdir('.')#当前目录下使用（‘.’）
    #使用列表解析，注意只能是元组
    title=[name for name in os.listdir('.') if name.endswith(('.sh','.py'))]
    print 2,title
    print 3,os.stat('a.sh').st_mode#十进制的权限
    print 4,oct(os.stat('a.sh').st_mode)#644是权限
    #修改权限，用户的掩码
    os.chmod('a.sh',os.stat('a.sh').st_mode|stat.S_IXUSR)#stat.S_IXUSR是可执行,与原来的或
    print 5, oct(os.stat('a.sh').st_mode)
    #如何调整字符串中文本的格式
    #解决方案，使用正则表达式re.sub()方法做字符串替换，利用字符串表达式捕获组，捕获每个部分的内容，替换字符串中调整各个捕获组的顺序
    log='2018-03-18 17:59:27 status installed libc-bin:amd64 2.19-0ubuntu6.5'
    print 6,re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)#这里的r代表原始字符串，不需要\\1
    print 7, re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)#给每个组起个别名




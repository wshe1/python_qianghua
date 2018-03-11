#-*- coding: UTF-8 -*-
#如何实现历史记录，显示最近5次的记录
from collections import deque
from random import randint
import pickle #将文件对象存储到对象中
N=randint(0,100)
history=deque([],5)
def guess(k):
    if k==N:
        print 'right'
        return True
    elif k<N:
        print '%s is less than N'%k
    else:
        print '%s is greater-than N' % k
    return False

if __name__=='__main__':
    q=deque([],5)
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    q.append(5)
    print 1,q
    q.append(6)
    q.append(7)
    print 2,q

    while True:
        line=raw_input('plesae input a number:')
        if line.isdigit():#判断是否是数字
            k=int(line)
            history.append(k)
            if guess(k):
                pickle.dump(history,open('history','w'))#将history对象写入到history文件中
                break
        elif line=='history'or line=='h':
            print 3,list(history)

    q2=pickle.load(open('history'))#从history中载入对象
    print 4,list(q2)




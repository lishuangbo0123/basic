from threading import Thread
def func(name):
    for i in range(1000):
        print(name,i)

class MyThread(Thread):
    def __init__(self):

    def run(self):
        for i in range(1000):
            print("zz",i)

if __name__ == '__main__':
    # t = Thread(target=func,args=("周杰伦",))  #第一种方式使用线程
    # t.start()
    t = MyThread()  #第二种方式使用线程
    t.start()   #start默认是调用线程模块中的run函数，上面那块也是重写run函数
    for i in range(1000):
        print("main",i)


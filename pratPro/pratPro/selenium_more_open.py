from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pratPro.webdriver_start_parmas import get_driver
import threading
from concurrent.futures import ThreadPoolExecutor #线程池和进程池
import time

# bro1 = get_driver()
# bro2 = get_driver()
# bro3 = get_driver()
# bro4 = get_driver()
# bro5 = get_driver()
# bro6 = get_driver()
class selenium_false:

    def __init__(self,name):
        self.name = name

    def do_something(self):
        for i in range(1000):
            print('子线程', i)
        print(f'{self.name}做事情做事情{time.localtime(time.time())}')


bro1 = selenium_false('bro1')
bro2 = selenium_false('brp2')
bro_list = [bro1,bro2]

def fun(a):

    t = threading.Thread(target=func,args=(a,))
    t.start()

def func(a):
    for i in range(10):
        time.sleep(1)
        print(f'{a}子线程', i)

    return funcc()

def funcc():
    print('funcc')


fun('aaaa')
fun('bbbb')
fun('cccc')
# test = ['1asd','2bfd','3re','4fds','5rew','6rewqq','7dfsxz','8uiy','9das','10gfdr']






# with ThreadPoolExecutor(6) as t:#开辟50条线程
#     for i in range(10):   #假设有4个任务
#         future = t.submit(fun,bro = bro_list[i%2])
#         print(f'拿到了第{i}次任务的结果{future.result()}')


# def task1():
#     # task 1 code
#     time.sleep(4)
#     print(f'11111做事情做事情{time.localtime(time.time())}')
#
# def task2():
#     # task 2 code
#     time.sleep(4)
#     print(f'222222做事情做事情{time.localtime(time.time())}')
#
# # create two thread
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
#
# # start the thread
# t1.start()
# t2.start()
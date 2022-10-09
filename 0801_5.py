import os
print(__file__)   #返回当前文件路径
print(os.path.dirname(__file__))  #返回file所在文件夹的路径
print(os.getcwd())  #当前程序的执行路径
print(os.chdir(r"c:\\"))#修改当前程序的执行路径  这样修改之后执行程序的路径中没有此程序，所以会报错文件找不到
os.rename("/Users/lee/Desktop/python","/Users/lee/Desktop/python目标")   #可以修改文件名也可以修改文件夹名
print(os.path.exists("/Users/lee/Desktop/python目标/python反爬虫.jpg")) #判断路径(文件、文件夹)是否存在
print(os.path.isfile("/Users/lee/Desktop/python目标/python反爬虫.jpg")) #判断路径是否是文件。无法判断文件夹
print(os.path.isdir("/Users/lee/Desktop/python目标/")) #判断路径是否是文件夹。无法判断文件
for k,v in os.environ.items():  #获取系统环境变量
    print(k,"==>",v)
os.mkdir("/Users/lee/Desktop/python目标/1")   #创建单层文件夹，如果已存在就报错
os.makedirs("/Users/lee/Desktop/python目标/5/2/3/4") #创建多层文件夹
list = os.listdir("/Users/lee/Desktop/python目标") #获取文件夹下所有子文件
for i in list:
    print(i)
with open("/Users/lee/Desktop/python目标/3.txt","w") as f:   #创建文件
    pass




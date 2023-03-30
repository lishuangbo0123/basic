import math
import random
print(math.pi)  #π
print(math.e)   #自然常数e
print(math.ceil(3.3))   #向上取整
print(math.floor(3.3)) #向下取整
print(math.pow(2,3)) #2的3次方
print(math.log(8,2))#log以2为底的8的对数
print(math.log(math.pow(math.e,2))) #不写底数就是默认e
print(math.sqrt(4)) #平方根计算
print(math.sin(math.pi)) #正余弦切
print(math.degrees(math.pi)) #弧度转角度
print(math.radians(90)) #角度转弧度

print(random.random()) #0-1之间的数
print(random.uniform(1,150)) #1-150之间的数且不重复
print(random.randint(1,150)) #1-150之间的正数  且不重复
print(random.choice("ewqewq")) #从给定的序列中随机抽取元素  字符串、列表、元组、
a = [0,1,2]
random.shuffle(a)  #打乱列表中元素的顺序。因为是打乱原序列，所以原来序列必须是可变的，所以数组可以用此方法，而元组不行
print(a)


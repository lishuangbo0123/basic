from datetime import datetime

# f = open('mybaidu.html',"a")
# now = str(datetime.now()) + "\n"
# print(f.write(now))

# f = open("mybaidu.html")
# print(f.read())
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# print(f.readline(),end = "")
# for i in f.readlines():
#     print(i,end = "")
# for i in f:
#     print(i , end = "")

# f = open("mybaidu.html","w")
# try:
#     list1 = []
#     for i in range(10):
#         list1.append(str(i))
#     f.writelines(list1)
# except OSError:
#     pass
# finally:
#     f.close()

# with会默认close
with open("mybaidu.html") as f:
    print(f.read())




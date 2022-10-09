import test_1
import test_2
import sys
# print(__name__)
# test_1.test_go()
# print(dir(test_1))
#
# str = '1'
# print(dir(str))
# print(test_1.jia(3,2))
# print(dir(test_2))
# print(sys.path)

# print(sys.platform)
# print(sys.argv[2])
if len(sys.argv) < 2:
    print("缺少参数")
    sys.exit()
for i in sys.argv:
    print(i)

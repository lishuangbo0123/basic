from io import StringIO
from  io import  BytesIO
# f = StringIO()
# f.write("aaa")
# f.write("  ")
# f.write("bbb")
# print(f.getvalue())

# f = StringIO("Hello\nWorld\n!!")
# while True:
#     s = f.readline()
#     if s == "":
#         break
#     print(s.strip())

f = BytesIO()
f.write("您好".encode("utf-8"))
print(f.getvalue())
print(f.getvalue().decode("utf-8"))

f= BytesIO(b'\xe6\x82\xa8\xe5\xa5\xbd')
print(f.read().decode("utf-8"))
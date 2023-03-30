import re

# match用法，从第一个开始正则匹配
# pattern = re.compile(r"\d+")
# str = pattern.match("123one21")
# print(str)
# str = pattern.match("one123",3,5)
# print(str.group())
# str = re.match(r"\d+","123one",re.I)
# print(str)

# search 是匹配符合正则的第一个结果
# pattern = r'\d+'
# str = re.search(pattern,'one123dsaew23',re.I)
# print(str)
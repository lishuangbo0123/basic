import re
s = r'eating apple seeing paper watching movie'
m1 = re.findall(r'(\b\w+?)ing',s)
print(m1)
# ?=  正预测先行断言
# ?<= 正回顾后发断言
# ?!  负预测先行断言
# ?<! 负回顾后发断言

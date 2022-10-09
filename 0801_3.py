import pickle
str = "您好，世界"
with open("mybaidu.html","wb") as f:
    pickle.dump(str,f)

with open("mybaidu.html","rb") as f:
    a = pickle.load(f)
    print(a)
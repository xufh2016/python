import os

currentPath = os.getcwd()
print(currentPath)
res = os.stat(currentPath)
print(res)
os.chdir("../")
currentPath = os.getcwd()
data = os.walk(currentPath)
for root, dirs, files in data:
    print(f"root:{root}")
    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))

# see = os.listdir(currentPath)#返回的是一个列表list
# # see = os.walk(currentPath) # 递归所有文件夹
# print(type(see))
# for item in see:
#     print(item)
# print(currentPath)
f = os.open("D://test/helloworld.txt", os.O_RDWR | os.O_CREAT)
os.write(f, b"Hello world,this is Python")

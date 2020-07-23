# 文件的读写

# 写--------------------

# import time
# now = time.strftime("%y~%m~%d %H:%M:%S")  # 目前时间、格式

# text = input("shuru:")
# # utf8 中文输入格式    目前于demo05同文件夹 相对位置 在名字中可以手动载入地址
# with open("wendang.txt", "a", encoding="utf8") as a:
#     a.write(now+"\n")
#     a.write("----------------------"+"\n")
#     a.write(text+"\n")  # \n 换行  \t 缩进
#     a.write("----------------------"+"\n")

# 读------------------
with open("wendang.txt", "r", encoding="utf8") as b:
    text = b.readlines()  # 数组方式读取
    for i in text:  # 遍历读取
        print(i)

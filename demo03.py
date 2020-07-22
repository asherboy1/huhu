# 30绿 25红 3黄

# import time
# while True:
#     for i in range(30, 0, -1):
#         time.sleep(1)
#         print("绿色剩余", i, "秒")

#     for k in range(3, 0, -1):
#         time.sleep(1)
#         print("黄色剩余", k, "秒")

#     for j in range(25, 0, -1):
#         time.sleep(1)
#         print("红色剩余", j, "秒")

# 注册功能 账号全数字5-8位  密码 首字母位小写英文 6-12位

a = []
b = []
c = input("输入注册的账号")
if c.isdigit() and len(c) > 4 and len(c) < 9:  # 判断字符串是否为纯数字c.isdigit()
    a.append(c)

else:
    print("注册格式不正确")
    print("注册失败")
    exit()


d = input("密码")
# 判断首字母是否为英文小写
if d[0] not in "abcdefghijklmnopqrstuvwxyz" or len(d) < 5 or len(d) > 12:
    print("密码格式不正确")
    print("注册失败")
    exit()
else:
    b.append(d)

print("注册成功")
print("注册账号为：", a)
print("账号密码为：", b)

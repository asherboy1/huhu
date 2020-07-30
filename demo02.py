# 判断

# a = 1
# b = 2
# if a < b:
#     print("ok")

# age = input("insert age:")
# if type(age) is not int:
#     exit()
# if age > 60:
#     print("get retired")
# elif age > 30:
#     print("you need work hard")
# elif age > 20:
#     print("you need get plan poperly")


# a = {}
# a.update(name=77, age=10, tel=20)
# if "age" not in a:
#     print("ok")
#     print(a)
# else:
#     print("no")

# ----------------------------------------
# 成绩录入 5个 分开存放60

a = []
b = 0
high = {}
low = {}
e = 0
k = 0
while b < 5:
    a.append(input("名字:"))
    b = b + 1

print("所有学生", a)

while e < len(a):
    k = int(input("输入"+a[e]+"成绩:"))
    if k > 60:
        high[a[e]] = k  # a[e]相当于key，k相当于value 添加入字典
    else:
        low[a[e]] = k
    e = e + 1

print("及格", high)
print("不及格", low)

# -------------------------------------
a = "cscasdasd"
for i in a:
    print(i)

b = list(range(10))

print(b)


# 99乘法表--------------------
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", i*j, end="   ")
    print()  # 换行

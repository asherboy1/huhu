# a = input("请输入"  )
# print("input contend",a)

# print(type(a))
# print(type("哈哈"))
# print(type(112))

# a = float(input("输入a的值"))
# b = float(input("输入b的值"))


# print("he",a+b)

# a = 'nvjfvkanvnaioenioenvoinvioenv'
# b = "sacaslxmlaks"
# print("he", len(a)+len(b))


# c = (1, 2, 3, 4, "haha", True)  # 空元组
# print(c)
# print(c[4])
# print(c.index("haha"), c.count(2))

# b = (c, 1)
# print(b[0][4])
# print(c[1:5]) #左闭右开

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.append(19)
# print(a)
# a.insert(1, 28)
# print(a)
# b = a.pop(1)
# print(a, b)

# c = [0, 1, True, False]
# print(c.count(1))
# print(c.count(0))

# b = c.remove(1)
# print(b)

# a = ((4, 5))
# b = ((a, 1))
# print(a)
# print(b[0])

# a = {"name": "hu", "age": "22"}
# print(a["name"], a["age"])
# a["name"] = 'huhu'
# print(a["name"])
# b = a.get("name")
# print(b)
# a.update(name='lolo')
# print(a.get("name"))


d = {}

d.update(name="xixi", age=18, tel=5566)

print(d)
a = input("name:")
b = input("age:")
c = input("tel:")

d.update(name=a, age=b, tel=c)
print(d)

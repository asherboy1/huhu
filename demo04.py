# -------------------------

# class 声明类的名字
# 然后类的名字首字母必须大写
# 面向对象的编程

# ----------------------------
# class Test():
#     def __init__(self):
#         self.id = "007"
#         self.age = "21岁"
#         self.grade = "及格"

#     def techang(self, num):
#         if num == 1:
#             print("lanqiu")
#         elif num == 2:
#             print("pingpang")
#         else:
#             print("zuqiu")

#     def xueli(self):
#         print("benke")

#     def work(self):
#         print("rk")

# # 类的实例化
# laohu = Test()

# laohu.xueli()
# laohu.techang(2)

# ---------------------------------
# class Test():
#     def __init__(self, id, age, grade):   #自定义 以输入为准
#         self.id = id
#         self.age = age
#         self.grade = grade

#     def techang(self, num):
#         if num == 1:
#             print("lanqiu")
#         elif num == 2:
#             print("pingpang")
#         else:
#             print("zuqiu")


# # 类的实例化
# laohu = Test("007", "20", "80")

# print("mm", laohu.grade)

# -----------------------------------------
class Car():
    def __init__(self, pingpai, color, neishi):
        self.pingpai = pingpai
        self.color = color
        self.neishi = neishi

    def fly(self):
        print("qifei!")

    def speed(self):
        print("speed up!")

    def div(self):
        print("swim")


class Newcar(Car):  # 类的继承
    def fly(self):
        print("jiangluo!")


zz = Newcar("cc", "red", "haohua")

print(zz.color)
zz.speed()
zz.fly()  # 类的重写 将父类的相同方法的内容 覆盖掉了

# object 所有类的祖宗

# Car  父类    Newcar   子类

dict1 = {
    "tony":7777,
    "lili":8888
}

dict2 = {
    "tom":9999
}

dict3 = {**dict1,**dict2}   #关键！！！ **为解包字典操作

for i,j in dict3.items():
    print(i,j)


list1 = ['tony']
list2 = ['tom']
list3 = [*list1,*list2]     #* 可解包 数组 元组

print(list3)
#------------------

name = "Tony Jin"

firstname,secondname = name.split()     #直接将name 按空格分开  序列解包

print(firstname,secondname)

class sanyuan:
    def cla(self,num : int = 0) -> bool:
        return True if num > 60 else False      #三元表达式

# a = sanyuan()
# point = int(input())
# mm = a.cla(num = point)
# print(mm)

#------------------------lambda式

test1 = lambda a,b:a+b  #相当于 一个a+b的函数 缩略版 a,b 相当于传入的参数 返回函数指针的实例对象
print(test1(a=10,b=11))

#--------------------map

list1 = [1,2,3,4]

def squ(num):
    return num**2

result = map(squ,list1)    # 表示将list1里的每一个元素 载入squ函数中 返回其值
print(type(result))     # 返回的是map类型 可以将其数组化
print(list(result))

tuple1 = (5,6,7,8)          # 元组也行
result2 = map(lambda x:x**2,tuple1)      # 合并 
print(list(result2))

testzz = [i for i in list1 if i > 2 ]  # 正则表达式 赋值
print(testzz)

f = lambda x,y:x if x > y else y
print(f(2,3))
list1 = [
    ('tony',1),
    ('tom',2),
    ('lili',1.2),
    ('lucy',1.8)
]

newlist1 = sorted(list1,key = lambda x : x[1],reverse = True)  # x 作为key值 仅为一个单位传入 x[1] 就为元组中第1号位  可以根据情况自定义用来排序的元素
print(newlist1)

print(sorted(list1))

test1 = [0,2,4,6]
test2 = [1,3,5,7]

print(list(map(lambda x,y:x+y,test1,test2)))  # 同时传入两个列表 使其参数相加

from functools import reduce

print(reduce(lambda x ,y : x + y ,range(1,101)))  # reduce 归约 lambda 虽然有两个参数 但reduce可将上一个结果 传入
print(reduce(lambda x , y: x * y ,range(5,8),10))      # 第三个参数位初始值 即为第一个x

res = filter(lambda x:True if x%5 == 0 else False,test2)   # filter需要转换 满足条件 即留下  x%5 为条件 可以自设传入 达到根据条件 挑选的目的
print(list(res))
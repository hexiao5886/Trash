# 反射是指 程序能够访问、检测和修改 它本身状态或行为 的能力
# 反射 in python-面向对象 : 通过字符串的形式操作对象相关的属性、方法

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking...")

p = Person("Alex", 22)

if hasattr(p, "name"):
    print("拥有该属性。")
else:
    print("无效属性。")

a = getattr(p, "age")
print(a)
"""
# input "walk", print("walking...")
user_cmd = input(">>:").strip()
if hasattr(p, user_cmd):
    func = getattr(p, user_cmd)
    func()
"""
# setattr
setattr(p, "sex", "male")
print(p.sex)

def talk(self):
    print("%s is speaking now." % self.name)
setattr(p, "speak", talk)                       # 对实例 绑定方法
p.speak(p)
setattr(Person, "speak2", talk)                 # 对类  绑定方法
p.speak2()


import sys
for k, v in sys.modules.items():
    # print(k, v)
    if k == "__main__":
        print(v)
        # <module '__main__' from 'D:/Engineering_Study/Pycharm/Projects_Data/振动信号分析/面向对象之 反射.py'>
        # 这就是正在运行的module 相当于一个类的self

print(sys.modules[__name__])    # 效果同上
mod = sys.modules[__name__]
print(mod.p)                    # <__main__.Person object at 0x000001EEECD9A400>

import test_mod
if hasattr(test_mod, "hi"):
    f = getattr(test_mod, "hi")
    f()
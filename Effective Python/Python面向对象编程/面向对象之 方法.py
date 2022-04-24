# 类方法 @classmethod
# 静态方法 @staticmethod
# 属性方法 @property

class Dog():
    Dog_Type = "牧羊犬"
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def do(self):
        print(self.name)        # 能访问实例变量

    @classmethod
    def do2(cls):
        print(cls.Dog_Type)     # 能访问类变量

    @staticmethod
    def run():
        print("I am running.")          # 不能访问实例变量，也不能访问类变量；只是名义上在类内

    @property
    def walk(self):
        print("%s am walking." % self.name)          # 把方法变成了属性，调用时不用括号了

    # 属性方法 应用
    @property
    def flight_status(self):
        self.status = 1          # 这里做简化，实际可能通过调用函数得到（查询）status
        if self.status == 1:
            print("arrived.")
        else:
            print("cancelled.")

    @flight_status.setter
    def flight_status(self, status):
        self.status = status
        print("status changed to", self.status)


d = Dog("Alice", None)
# test of 属性方法
# d.walk                  # Alice am walking.
# d.walk()                # TypeError: 'NoneType' object is not callable   Alice am walking.
# d.flight_status         # arrived. （输出查询结果）
# d.flight_status = 0     # 手动修改 status





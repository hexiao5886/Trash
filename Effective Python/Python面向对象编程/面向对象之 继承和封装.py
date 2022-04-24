# Python 面向对象

class person():
    animal_type = "哺乳动物"
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height
        self.partner = None

    def make_relationship(self, another):
        self.partner = another
        another.partner = self

    def fight(self):
        print("%s is fighting." % self.name)

"""
# test 1: 对象之间关联
He = person("Richard", "male", 188)
She = person("Amy", "female", 177)
He.make_relationship(She)
print(He.partner.name, She.partner.name)
"""
# 继承 #

# 继承父类 重写父类初始化和方法
class soldier(person):
    def __init__(self, name, sex, height, fight_capacity):
        # person.__init__(self, name, sex, height)
        super().__init__(name, sex, height)
        self.fc = fight_capacity            # 下面是子类新添加的属性
        self.__life_val = 100               # 前面__ 代表私有变量，只有类的内部可访问

    def fight(self):
        # person.fight(self)
        super().fight()
        self.__command("forward")
        print("I am a real soldier.")


    def get_life_val(self):
        print("My lif val is %s" % self.__life_val)

    # 私有属性
    def __command(self, cmd):
        print("I received the command:", cmd)

# 封装 #
"""
# test 2: 私有属性
us_captain = soldier("美国队长", "male", 199, 420)
# print(us_captain.__life_val)       Error!!
us_captain.get_life_val()
# test 3： 私有方法
us_captain.fight()
"""

"""
# test 4: 外部访问私有属性、方法
batman = soldier('蝙蝠侠', 'male', 156, 440)
batman._soldier__life_val = 160
batman.get_life_val()
batman._soldier__command("go back home")
"""

# 多态 #
# empty
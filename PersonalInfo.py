from random import random
import AbilitySettingTool

class PersonalInfo:
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint):
        self.name = name
        # birth格式为'xxxx.xx'（eg: 1995.03）
        self.birth = birth
        self.country = country
        self.sex = sex
        # 范围[-100,100]
        self.attitude = attitude
        # 履历（list: [[公司1, 开始时间, 结束时间], [公司2, 开始时间, 结束时间]]）
        self.record = record
        # 月薪
        self.salary = salary
        self.company = company
        # 范围[0, 100]
        self.__workpoint = workpoint

    def age(self, time):
        # 此处time为年份即xxxx
        return time - int(self.birth[0:4])

    def add_record(self, company, time):
        # 此处time为原始数据即xxxx.xx
        # 无公司(None)也看作是一个company
        # 更新上一个公司list的结束时间
        self.record[-1][2] = time
        # 创建新公司list的公司名和开始时间
        self.record.append([company, time, 'until now'])


class Employee(PersonalInfo):
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ability={}):
        PersonalInfo.__init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint)
        # 能力为一个list包含各项能力值的dict和等级评分(eg: {'领导力': 2, '训练': 1, 'level': 1})
        self.ability = ability

    def set_ability(self):
        self.ability['SoundTeach'] = random.randint(0, 10)
        self.ability['DanceTeach'] = random.randint(0, 10)
        self.ability['ShapeTeach'] = random.randint(0, 10)
        self.ability['ClothDesign'] = random.randint(0, 10)
        self.ability['PR'] = random.randint(0, 10)
        self.ability['Business'] = random.randint(0, 10)
        self.ability['StarEyesight'] = random.randint(0, 10)
        # 基础工资加能力值加成(时薪)
        for ability in self.ability:
            self.salary += self.ability[ability]

    def set_level(self):
        # 求总值
        a_sum = 0
        for ability in self.ability:
            a_sum += self.ability[ability]
        # 分类
        level = a_sum//7
        self.ability['level'] = level

    def toward_attitude(self, person):
        pass

    def get_attitude(self, person):
        pass


class Trainee(PersonalInfo):
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint):
        PersonalInfo.__init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint)
        # 能力为一个list包含各项能力值的dict和等级评分
        self.ability = {}

    def set_ability(self):
        # 长度为2的list表示CA与PA
        self.ability['appearance'] = AbilitySettingTool.ast(20)
        self.ability['figure'] = AbilitySettingTool.ast(20)
        self.ability['singing'] = AbilitySettingTool.ast(20)
        self.ability['dancing'] = AbilitySettingTool.ast(20)
        # 特长为
        self.ability['specialty'] = []
        # 基础工资加能力值加成(时薪)
        for ability in self.ability:
            self.salary += self.ability[ability]




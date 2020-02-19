import random


class PersonalInfo:
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ID):
        # ID 生成
        self.__ID = ID
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
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ID):
        PersonalInfo.__init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ID)
        # 能力为一个list包含各项能力值的dict和等级评分(eg: {'领导力': 2, '训练': 1, 'level': 1})
        self.ability = {}

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
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ID):
        PersonalInfo.__init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint, ID)
        # 能力为一个list包含各项能力值的dict和等级评分
        self.ability = {}

    def set_ability(self):
        # 长度为2的list表示CA与PA 150为理论最终上限
        self.ability['appearance'] = [random.randint(0, 100), random.randint(0, 50)]
        self.ability['figure'] = [random.randint(0, 100), random.randint(0, 50)]
        self.ability['singing'] = [random.randint(0, 100), random.randint(0, 50)]
        self.ability['dancing'] = [random.randint(0, 100), random.randint(0, 50)]
        # 特长为
        self.ability['specialty'] = ['None']
        # 基础工资加能力值加成(时薪)
        for ability in self.ability:
            if isinstance(self.ability[ability][0], int):
                self.salary += self.ability[ability][0]

    def set_level(self):
        ca_sum = 0
        pa_sum = 0
        # 求CA等级和PA等级
        for ability in self.ability:
            if isinstance(self.ability[ability][0], int):
                ca_sum += self.ability[ability][0]
                pa_sum += self.ability[ability][1]
        # 分级
        self.ability['level'] = [ca_sum//40, pa_sum//20]


if __name__ == "__main__":
    i = 0
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while i < 10000:
        a = Trainee('a','1999','b','b','c','d',1000,'b',100,'T1')
        a.set_ability()
        a.set_level()
        print(a.ability)
        ca_level = a.ability['level'][0]
        if ca_level == 0:
            a1 += 1
        if ca_level == 1:
            a2 += 1
        if ca_level == 2:
            a3 += 1
        if ca_level == 3:
            a4 += 1
        if ca_level == 4:
            a5 += 1
        if ca_level == 5:
            a6 += 1
        if ca_level == 6:
            a7 += 1
        if ca_level == 7:
            a8 += 1
        if ca_level == 8:
            a9 += 1
        if ca_level == 9:
            a10 += 1

        i += 1
    level = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
    print(level)


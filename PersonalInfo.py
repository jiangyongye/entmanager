class PersonalInfo:
    def __init__(self, name, birth, country, sex, attitude, record, salary, company, workpoint):
        self.name = name
        # birth格式为xxxx.xx（eg: 1995.03）
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
        self._workpoint = workpoint

    def age(self, time):
        return time - self.birth

    def add_record(self, company, time):
        # 自由身也算入company
        # 更新上一个公司list的结束时间
        self.record[-1][2] = time
        # 创建新公司list的公司名和开始时间
        self.record.append([company, time, 'until now'])




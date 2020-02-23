class Groups:
    def __init__(self, name, members, company, reputation, style, popularity, fans):
        self.name = name
        # 成员用list储存？
        self.members = members
        self.company = company
        # 知名度
        self.reputation = reputation
        self.style = style
        # 人气值
        self.popularity = popularity
        self.fans = fans
        self.works = {}
        # 契合度
        self.__compatibility = 0
        self.honor = {}

    def add_works(self):
        pass

    def set_compatibility(self):
        pass

    def add_honor(self):
        pass

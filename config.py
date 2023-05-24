class ParseResult:
    def __init__(self, title: str, price: str, link: str):
        self.title = title
        self.link = link
        self.price = float(price.replace(',', '.')[:4])


        if len(self.title.split(',')) == 1:
            self.weight = float(self.title.split(' ')[-2])
        else:
            self.weight = float(self.title.split(',')[-1].strip().replace('г', ''))
        self.profit = self.price / self.weight

    def __str__(self):
        return f'{self.title}, {self.price}p., {self.link}'

    def __repr__(self):
        return f'{self.title, self.price, self.link}'

    def __lt__(self, other):
        self_price = self.price
        other_price = other.price
        return self_price < other_price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


class OutputValues:
    def __init__(self, res: list[ParseResult], file):
        self.res = [coffe_obj for coffe_obj in sorted(res)]
        self.file = file

    def printing(self):
        print('Кофе растворимый:', file=self.file)
        for i in self.res:
            print(i, file=self.file)
        return 'Ready'

    def profitable(self):
        print('Топ 5 самых выгодных:', file=self.file)
        for i in range(5):
            print(f'{i+1}){sorted(self.res, key=lambda x: x.profit)[i]}', file=self.file)
        return 'Ready too'

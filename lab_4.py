# Класс Human
class Human:
    default_name = "Катя"
    default_age = 20

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.__money)
        if self.__house:
            print("House:", self.__house.final_price(0))
        else:
            print("House: None")

    @staticmethod
    def default_info():
        print("Default Name:", Human.default_name)
        print("Default Age:", Human.default_age)

    def __make_deal(self, house, money):
        self.__money -= money
        self.__house = house

    def earn_money(self):
        self.__money += 100

    def buy_house(self, house, discount=0):
        if self.__money >= house.final_price(discount):
            self.__money -= house.final_price(discount)
            self.__house = house
            self.__house.owner = self
            return True
        else:
            print("Недостаточно денег на счете")
            return False


# Класс House
class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price
        self.owner = None

    def final_price(self, discount):
        return self.price - discount


# Класс SmallHouse
class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


# Тесты
Human.default_info()

human1 = Human("Маша", 34)
human1.info()

house1 = SmallHouse(50000)
human1.buy_house(house1, 10000)
human1.info()

human1.earn_money()
human1.buy_house(house1, 10000)
human1.info()
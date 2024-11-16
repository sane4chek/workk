def txt_color(text, color):
    col_dic = {'black': 30, 'red': 31, 'yellow': 32, 'orange': 33, 'blue': 34, 'violet': 35, 'grey': 37, 'white': 38}
    _color = color.lower()
    if _color in col_dic:
        print("\033[" + str(col_dic[_color]) + "m{}".format(text))
        print(f"\033[{col_dic['white']}m", end='')


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.set_color(color)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            txt_color(f"Нельзя сменить цвет на {new_color}", 'red')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()

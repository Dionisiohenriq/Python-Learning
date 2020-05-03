class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def format_data(self):
        print(f'{self.__dia:02d}/{self.__mes:02d}/{self.__ano:4d}')

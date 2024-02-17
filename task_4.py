class Screen:
    """Монитор"""
    def __init__(self, name: str, width: int, height: int, dpi: int):
        """
        Инициализация объекта
        :param_name name: наименование монитора
        :param_name width: ширина разрешения экрана
        :param_name height: высота разрешения экрана
        :param_name dpi: Плотность пикселей (количество пикселей на дюйм)
        """
        self._name = name
        self._width = width
        self._height = height
        self._dpi = dpi
        self._graphics_mode = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Атрибут name должен быть строкой")
        name = value.strip()
        if name == '':
            raise ValueError("Атрибут name не должен быть пустым")
        self._name = name

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Атрибут width должен быть целым числом")
        if value <= 0:
            raise ValueError("Атрибут width должен быть положительным")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Атрибут height должен быть целым числом")
        if value <= 0:
            raise ValueError("Атрибут height должен быть положительным")
        self._height = value

    @property
    def dpi(self):
        return self._dpi

    @dpi.setter
    def dpi(self, value):
        if not isinstance(value, int):
            raise TypeError("Атрибут dpi должен быть целым числом")
        if value <= 0:
            raise ValueError("Атрибут dpi должен быть положительным")
        self._width = value

    def update_frame(self):
        """Процедура обновления текущего кадра"""
        pass

    def toggle_graphics_mode(self) -> bool:
        """Процедура переключения графического и алфавитно-текстового режимов"""
        self._graphics_mode = not self._graphics_mode
        return self._graphics_mode

    def __str__(self) -> str:
        """Строковое описание объекта для пользователя"""
        return f'Screen "{self._name}": {self._width}x{self._height} (dpi: {self._dpi})'

    def __repr__(self) -> str:
        """Репрезентация объекта"""
        return f'Screen(name="{self._name}", width={self._width}, height={self._height}, dpi={self._dpi})'


class CrtScreen(Screen):
    """Монитор по технологии электронно-лучевой трубки (CRT)"""
    def __init__(self, name: str, width: int, height: int, dpi: int, frequency: int):
        """
        Инициализация объекта
        :param_name name: наименование монитора
        :param_name width: ширина разрешения экрана
        :param_name height: высота разрешения экрана
        :param_name dpi: Плотность пикселей (количество пикселей на дюйм)
        :param_name frequency: Частота обновления изображения (прохождения полного цикла сканирования)
        """
        super().__init__(name, width, height, dpi)
        self._frequency = frequency

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if not isinstance(value, int):
            raise TypeError("Атрибут frequency должен быть целым числом")
        if value <= 0:
            raise ValueError("Атрибут frequency должен быть положительным")
        self._width = value

    def __scan_line(self, i_line: int):
        """
        Вывод очередной строки электронно-лучевой трубкой
        (служебный метод, вспомогательный для процедуры вывода кадра output_frame)
        :param_name i_line: Номер строки сканирования
        """
        pass

    def update_frame(self):
        """
        Процедура обновления текущего кадра.
        В ЭЛТ-экранах (CRT) процедура осуществляется полинейно
        """
        for i_line in range(self.height):
            self.__scan_line(i_line)

    def toggle_graphics_mode(self) -> bool:
        """Процедура переключения графического и алфавитно-текстового режимов"""
        return super().toggle_graphics_mode()

    def __str__(self) -> str:
        """Строковое описание объекта для пользователя"""
        return f'CRT Screen "{self._name}": {self._width}x{self._height} (dpi: {self._dpi}, {self._frequency} Hz)'

    def __repr__(self) -> str:
        """Репрезентация объекта"""
        return f'CrtScreen(name="{self._name}", width={self._width}, height={self._height},' \
               f'dpi={self._dpi}, frequency={self._frequency})'


if __name__ == "__main__":
    # Write your solution here
    pass

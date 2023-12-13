from typing import Union, Optional


class Tone:
    def __init__(self, key_no: Optional[int], value: Union[int, float], velocity: Union[int, float]):
        """
        Создание и подготовка к работе объекта Нота

        :param key_no: номер клавиши от 0 до 127 (40 - это нота _ _-й октавы) или пустое значение (для паузы)
        :param value: длительность ноты (относительно целой ноты)
        например, 1 - целая нота, 0.75 - половинка с точкой, 0.5 - половинка)
        :param velocity: сила нажатия от 0.0 до 1.0

        Примеры:
        >>> tone = Tone(40, 1 / 2, 0.77)
        """
        if not isinstance(key_no, (int, type(None))):
            raise TypeError("Номер клавиши должен быть целым числом или пустым (для паузы)")
        if not (key_no is None or 0 <= key_no <= 127):
            raise ValueError("Номер клавиши должен быть в диапазоне [0..127]")
        self.key_no = key_no

        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0.0:
            raise ValueError("Длительность должна быть положительной")
        self.value = value

        if not isinstance(velocity, (int, float)):
            raise TypeError("Сила нажатия должна быть числом")
        if not (0.0 <= velocity <= 1.0):
            raise ValueError("Сила нажатия должна быть в диапазоне [0..1]")
        self.velocity = velocity

    def set_key_no(self, key_no: Optional[int]):
        """
        Установка номера клавиши или паузы

        :param key_no: номер клавиши от 0 до 127 (40 - это нота _ _-й октавы) или пустое значение (для паузы)

        Примеры:
        >>> tone = Tone(40, 1 / 2, 0.77)
        >>> tone.set_key_no(41)
        >>> tone.set_key_no(None) # превратили ноту в паузу
        """
        if not isinstance(key_no, (int, type(None))):
            raise TypeError("Номер клавиши должен быть целым числом или пустым (для паузы)")
        if not (key_no is None or 0 <= key_no <= 127):
            raise ValueError("Номер клавиши должен быть в диапазоне [0..127]")
        self.key_no = key_no

    def set_value(self, value: Union[int, float]):
        """
        Установка длительности

        :param value: длительность ноты (относительно целой ноты)
        например, 1 - целая нота, 0.75 - половинка с точкой, 0.5 - половинка)

        Примеры:
        >>> tone = Tone(40, 1 / 2, 0.77)
        >>> tone.set_value(0.75)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Длительность должна быть числом")
        if value <= 0.0:
            raise ValueError("Длительность должна быть положительной")
        self.value = value

    def set_velocity(self, velocity: Union[int, float]):
        """
        Установка силы нажатия

        :param velocity: сила нажатия от 0.0 до 1.0

        Примеры:
        >>> tone = Tone(40, 1 / 2, 0.77)
        >>> tone.set_velocity(0.8)
        """
        if not isinstance(velocity, (int, float)):
            raise TypeError("Сила нажатия должна быть числом")
        if not (0.0 <= velocity <= 1.0):
            raise ValueError("Сила нажатия должна быть в диапазоне [0..1]")
        self.velocity = velocity


class Pattern:
    def __init__(self, start_bar: int, instrument: str):
        """
        Создание и подготовка к работе объекта Паттерн

        :param start_bar: такт, с которого начинается паттерн
        :param instrument: инструмент

        Примеры
        >>> pattern = Pattern(1, 'Скрипка')
        """
        if not isinstance(start_bar, int):
            raise TypeError(" должен быть целым числом")
        if start_bar < 0:
            raise ValueError(" должен быть неотрицательным")
        self.start_bar = start_bar

        if not isinstance(instrument, str):
            raise TypeError("Инструмент должен быть строкой")
        if instrument == "":
            raise ValueError("Название инструмента не может быть пустым")
        self.instrument = instrument

        self.tones = []

    def set_start_bar(self, start_bar: int):
        """
        С какого такта в произведении начинается паттерн

        :param start_bar: такт, на котором находится начало паттерна

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.set_start_bar(2)
        """
        if not isinstance(start_bar, int):
            raise TypeError(" должен быть целым числом")
        if start_bar < 0:
            raise ValueError(" должен быть неотрицательным")
        self.start_bar = start_bar

    def set_instrument(self, instrument: str):
        """
        Назначение музыкального инструмента паттерну

        :param instrument: инструмент

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.set_instrument('Скрипка')
        """
        if not isinstance(instrument, str):
            raise TypeError("Инструмент должен быть строкой")
        if instrument == "":
            raise ValueError("Название инструмента не может быть пустым")
        self.instrument = instrument

    def transpose(self, n_by_tones: int):
        """
        Транспозиция паттерна

        :param n_by_tones: на сколько полутонов транспонировать паттерн

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.55))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.transpose(3) # повышение паттерна на 3 полутона
        >>> pattern.transpose(-1) # понижение паттерна на 1 полутон
        """
        ...

    def scale(self, coef: Union[int, float]):
        """
        Растягивание (замедление) или сжатие (ускорение) паттерна

        :param coef: коэффициент

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.55))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.scale(0.5)
        """
        ...

    def quantize(self, threshold_note_value: Union[int, float]):
        """
        Выравнивание паттерна по длительности

        :param threshold_note_value: длительность, по которой будет выровнен паттерн (относительно целой ноты)
        например, целая нота - 1.0, половинка с точкой - 0.75, половинка - 0.5)

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.55))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.45))
        >>> pattern.quantize(0.5)
        """
        ...

    def append_tone(self, tone: Tone) -> int:
        """
        Добавление ноты в конец паттерна

        :param tone: нота
        :return: позиция, на которую была добавлена нота

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.5))
        """
        ...

    def insert_tone(self, tone: Tone, position: int):
        """
        Вставка ноты в аккорд

        :param tone: нота
        :param position: позиция для вставки

        Примеры
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.5))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.5))
        >>> pattern.insert_tone(Tone(44, 1 / 2, 0.55), 1)
        """
        ...

    def delete_tone(self, position: int, index_in_chord: int = 0):
        """
        Удаление ноты по номеру из паттерна

        :param position: позиция ноты
        :param index_in_chord: номер ноты в аккорде (отсчет снизу), по умолчанию - 0 (самая нижняя нота в аккорде)

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.5))
        >>> pattern.append_tone(Tone(40, 1 / 2, 0.5))
        >>> pattern.insert_tone(Tone(44, 1 / 2, 0.55), 1)
        >>> pattern.delete_tone(1, 1)
        >>> pattern.delete_tone(1)
        """
        ...


class MusicalWork:
    def __init__(self, name: str, author: Optional[str], tempo: int):
        """
        Создание и подготовка к работе объекта Музыкальное произведение

        :param name: Название произведения
        :param author: Автор (необязательный параметр)
        :param tempo: Темп произведения, ударов в минуту

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название произведения должно быть строкой")
        if not len(name) > 0:
            raise ValueError("Название произведения не должно быть пустым")
        self.name = name

        if not isinstance(author, (str, type(None))):
            raise TypeError("Имя автора должно быть строкой или пустым")
        self.author = author

        if not isinstance(tempo, int):
            raise TypeError("Темп должен быть целым числом")
        if not (40 <= tempo <= 320):
            raise ValueError("Темп вне допустимого диапазона [40..320] bpm")
        self.tempo = tempo

        self.patterns = []

    def set_name(self, name: str):
        """
        Задание имени произведения

        :param name: Название произведения

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> musical_work.set_name("Сонатина 6 до-мажор")
        """
        if not isinstance(name, str):
            raise TypeError("Название произведения должно быть строкой")
        if not len(name) > 0:
            raise ValueError("Название произведения не должно быть пустым")
        self.name = name

    def set_author(self, author: Optional[str]):
        """
        Задание автора произведения

        :param author: Автор

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "Л.Моцарт", 140)  # инициализация экземпляра класса
        >>> musical_work.set_author("В.А.Моцарт")
        """
        if not isinstance(author, (str, type(None))):
            raise TypeError("Имя автора должно быть строкой или пустым")
        self.author = author

    def set_tempo(self, tempo: int):
        """
        Установка темпа

        :param tempo: новый темп (от 40 до 320 bpm - ударов в минуту)

        Пример:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> musical_work.set_tempo(160)
        """
        if not isinstance(tempo, int):
            raise TypeError("Темп должен быть целым числом")
        if not (40 <= tempo <= 320):
            raise ValueError("Темп вне допустимого диапазона [40..320] bpm")
        self.tempo = tempo

    def add_pattern(self) -> Pattern:
        """
        Добавление паттерна

        :return: созданный паттерн

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> pattern = musical_work.add_pattern()
        """
        ...

    def delete_pattern(self, pattern_no: int):
        """
        Удаление паттерна по номеру

        :param pattern_no: номер паттерна

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> musical_work.add_pattern()
        >>> musical_work.add_pattern()
        >>> musical_work.delete_pattern(0)
        """
        ...

    def get_pattern(self, pattern_no: int) -> Pattern:
        """
        Получение паттерна по номеру

        :param pattern_no: номер паттерна
        :return: паттерн (если существует)

        Примеры:
        >>> musical_work = MusicalWork("Сонатина №6", "В.А.Моцарт", 140)  # инициализация экземпляра класса
        >>> musical_work.add_pattern()
        >>> musical_work.add_pattern()
        >>> pattern = musical_work.get_pattern(0)
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

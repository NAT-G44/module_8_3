class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера, переданная строка должна состоять ровно из 6 символов')
        return numbers


# Пример использования
try:
    car = Car("Toyota", 1234567, "AB1234")
    print(f"Модель: {car.model}, VIN: {car._Car__vin}, Номера: {car._Car__numbers}")

except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)

import re


class ValidCarNumber:
    def __init__(self, number):
        self.number = number
    def is_valid(self):
        is_valid = re.search(r"0([0-9]{1})KG([0-9]{3})([A-Z]{3})", self.number)
        try:
            if self.number[is_valid.start():is_valid.end()] == self.number:
                print("Valid")
        except:
            print("Invalid")

number = input('Пример: 01KG777BAD \nВведите номер транспарта: ')
car = ValidCarNumber(number)
car.is_valid()
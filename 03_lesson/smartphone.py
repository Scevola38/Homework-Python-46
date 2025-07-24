class Smartphone:

    def __init__(self, brand, model, number):
        self.phone_brand = brand
        self.phone_model = model
        self.phone_number = number

    def say_brand(self):
        print("Марка телефона", self.phone_brand)

    def say_model(self):
        print("Модель телефона", self.phone_model)

    def say_number(self):
        print("Абонентский номер", self.phone_number)

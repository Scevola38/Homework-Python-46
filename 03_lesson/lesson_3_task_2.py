from smartphone import Smartphone

catalog = [
    Smartphone("iphone", "4", "+79102457845"),
    Smartphone("iphone", "5", "+79102457844"),
    Smartphone("iphone", "6", "+79102457843"),
    Smartphone("iphone", "7", "+79102457842"),
    Smartphone("iphone", "8", "+79102457841")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. "
          f"{smartphone.phone_number}.")

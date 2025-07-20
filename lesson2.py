#получить от пользователя оценку
rate_as_str = input("Оценить работу оператора от 1 до 5: ")
rate = int(rate_as_str)
if(rate<1):
   rate = 1
if(rate>5):
   rate = 5
print(rate)
user_login = "Dmitriy"
user_password = "Margerit39"

login = input("Логин: ")
password = input("Пароль: ")

if login == user_login and password == user_password:
   print("Вход выполнен!")
else:
   print("Неверный логин или пароль")
def is_year_leap(year):
    return True if year % 4 == 0 else False

yr = int(input("Введите год: "))
result = is_year_leap(yr)
print(f"год {yr}:{result}")
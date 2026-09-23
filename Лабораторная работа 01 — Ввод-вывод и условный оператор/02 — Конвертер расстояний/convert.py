print("Конвертер единиц измерения расстояния")
print("Доступные единицы: km, m, cm, mm, mi, yd")
ied = input("Исходная единица: ").lower()
ced = input("Целевая единица: ").lower()
value = float(input("Введите значение: "))

if ied == "km":
    meters = value * 1000
elif ied == "m":
    meters = value
elif ied == "cm":
    meters = value / 100
elif ied == "mm":
    meters = value / 1000
elif ied == "mi":
    meters = value * 1609.344
elif source == "yd":
    meters = value * 0.9144
else:
    meters = None

if meters is None:
    print("Неизвестная исходная единица")
elif ced == "km":
    result = meters / 1000
    print(f"Результат: {result:.6f} km")
elif ced == "m":
    result = meters
    print(f"Результат: {result:.6f} m")
elif ced == "cm":
    result = meters * 100
    print(f"Результат: {result:.6f} cm")
elif ced == "mm":
    result = meters * 1000
    print(f"Результат: {result:.6f} mm")
elif ced == "mi":
    result = meters / 1609.344
    print(f"Результат: {result:.6f} mi")
elif ced == "yd":
    result = meters / 0.9144
    print(f"Результат: {result:.6f} yd")
else:
    print("Неизвестная целевая единица")

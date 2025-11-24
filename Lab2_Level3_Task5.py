# приклад словника
cars = {
    "AA1234BB": ["Toyota", "Коваль"],
    "BC5678CA": ["BMW", "Іванов"],
    "AE1111PP": ["Toyota", "Мельник"],
    "KA2222AK": ["Audi", "Шевченко"]
}

# пошук за номером
number = input("Введіть номер авто: ")

if number in cars:
    print(f"Власник авто {number}: {cars[number][1]}")
else:
    print("Автомобіль з таким номером не знайдено.")

# статистика унікальних марок
brands = {info[0] for info in cars.values()}
print(f"Унікальні марки ({len(brands)}): {', '.join(brands)}")

import random

# генеруємо масив із 20 випадкових цілих чисел
arr = [random.randint(-100, 100) for _ in range(20)]
print("Згенерований масив:", arr)

# вибираємо числа, кратні 11
multiples = [x for x in arr if x % 11 == 0]

# сортуємо за спаданням
multiples.sort(reverse=True)

print("Числа, кратні 11 (спаданням):", multiples)

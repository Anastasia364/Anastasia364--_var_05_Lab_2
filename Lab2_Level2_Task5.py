# вводимо числа
nums = input("Введіть цілі числа через пробіл: ").split()

# перевірка коректності
for x in nums:
    if not x.lstrip("-").isdigit():
        raise ValueError("Помилка: усі значення мають бути цілими числами!")

nums = list(map(int, nums))

m = int(input("Введіть кількість рядків m: "))
n = int(input("Введіть кількість стовпців n: "))

if len(nums) != m * n:
    raise ValueError("Кількість чисел не відповідає розміру матриці")

# формування матриці
matrix = [nums[i*n:(i+1)*n] for i in range(m)]

print("Початкова матриця:")
for row in matrix:
    print(row)

# горизонтальне відображення (перевернути зверху вниз)
flipped = matrix[::-1]

print("Матриця після відображення по горизонталі:")
for row in flipped:
    print(row)

import numpy as np

# 1.    Створіть одновимірний масив з 200 випадкових чисел від -100 до 100.
arr = np.random.randint(-100, 101, 200)
print("Початковий масив:")
print(arr)

# 2.    Використовуючи маску, відфільтруйте всі додатні числа в масиві.
positive_numbers = arr[arr > 0]

print("\nДодатні числа:")
print(positive_numbers)

# 3.    Замініть всі від’ємні значення на нулі.
arr_no_negative = arr.copy()
arr_no_negative[arr_no_negative < 0] = 0

print("\nМасив після заміни від’ємних чисел на 0:")
print(arr_no_negative)

# 4.    Обчисліть середнє значення отриманого масиву.
mean_value = arr_no_negative.mean()

print("\nСереднє значення:")
print(mean_value)
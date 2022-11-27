
# 1. Преобразование введенной последовательности в список
array = list(map(int, input('введите числа через пробел: ').split()))
print(array)
# Запрашиваем у пользователя любое число
element = int(input('Введите число: '))
# проверяем ,есть ли введенное число в нашем списке,если нет , добавляем его в спиок
while element:
    if element not in array:
        array.append(element)
    else:
        break
# 2. Сортируем список по возрастанию элементов (методом пузырьков)
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
# 3. Установка позиции элемента алгоритмом двоичного поиска,
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


a = (binary_search(array,element, 0, len(array)-1))

print(a) # Позиция (индек) элемента
print(a-1,a) # Позиция (индекс) соседнего слева элемента и позиция самого элемента




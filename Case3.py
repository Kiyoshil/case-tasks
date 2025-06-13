def sum_negatives_between_min_max(arr):
    if not arr:
        return 0  # если массив пустой, возвращаем 0

    # Находим индексы минимального и максимального элементов
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    # Определяем границы диапазона (start и end)
    start = min(min_index, max_index)
    end = max(min_index, max_index)

    # Суммируем отрицательные элементы в этом диапазоне
    sum_neg = 0
    for i in range(start + 1, end):  # +1 чтобы не включать сам начальный элемент
        if arr[i] < 0:
            sum_neg += arr[i]

    return sum_neg


# Пример использования
N = int(input("Введите размер массива: "))
A = []
for i in range(N):
    num = int(input(f"Введите элемент {i + 1}: "))
    A.append(num)

result = sum_negatives_between_min_max(A)
print("Сумма отрицательных элементов между минимальным и максимальным:", result)
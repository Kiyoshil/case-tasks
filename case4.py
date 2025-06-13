def max_dragon_power(N):
    if N <= 1:
        return 0  # Нельзя разбить на несколько драконов

    max_product = 1
    # Оптимально разбиваем на тройки, а оставшуюся часть обрабатываем отдельно
    num_threes = N // 3
    remainder = N % 3

    if remainder == 1:
        # Если остаток 1, лучше взять одну тройку меньше и добавить две двойки (3+1 → 2+2)
        num_threes -= 1
        remainder = 4  # 3 + 1 → 2 + 2 (так как 2*2 > 3*1)
    elif remainder == 0:
        remainder = 1  # Чтобы не влиять на произведение (умножаем на 1)

    max_product = (3 ** num_threes) * (remainder if remainder != 1 else 1)
    return max_product


# Ввод данных
N = int(input("Введите количество голов драконьей стаи (0 < N < 100): "))
if N <= 0 or N >= 100:
    print("Некорректный ввод!")
else:
    result = max_dragon_power(N)
    print(f"Максимальная сила драконьей стаи из {N} голов: {result}")
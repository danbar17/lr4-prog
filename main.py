def set_calculator(file_path1: str, file_path2: str):
    """
    Калькулятор множеств.
    Читает данные из двух файлов и выполняет операции алгебры множеств в цикле.
    """
    try:
        # Чтение элементов из первого файла
        with open(file_path1, 'r', encoding='utf-8') as f1:
            set1 = set(f1.read().split())

        # Чтение элементов из второго файла
        with open(file_path2, 'r', encoding='utf-8') as f2:
            set2 = set(f2.read().split())

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден — {e.filename}")
        return

    print("--- Множества успешно загружены ---")
    print(f"Множество A: {set1}")
    print(f"Множество B: {set2}\n")

    while True:
        print("Доступные операции:")
        print("1. Объединение (A ∪ B)")
        print("2. Пересечение (A ∩ B)")
        print("3. Разность (A \\ B)")
        print("4. Разность (B \\ A)")
        print("5. Симметрическая разность (A △ B)")
        print("0. Выход (или введите 'exit')")

        choice = input("\nВыберите операцию: ").strip().lower()

        if choice in ('0', 'exit'):
            print("Выход из калькулятора. До свидания!")
            break

        if choice == '1':
            result = set1.union(set2)
            print(f"Результат объединения: {result}\n")
        elif choice == '2':
            result = set1.intersection(set2)
            print(f"Результат пересечения: {result}\n")
        elif choice == '3':
            result = set1.difference(set2)
            print(f"Результат разности (A - B): {result}\n")
        elif choice == '4':
            result = set2.difference(set1)
            print(f"Результат разности (B - A): {result}\n")
        elif choice == '5':
            result = set1.symmetric_difference(set2)
            print(f"Результат симметрической разности: {result}\n")
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт от 0 до 5.\n")

set_calculator('set_a.txt', 'set_b.txt')

def read_file(file_path, read_mode='full'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            if read_mode == 'full':
                content = file.read()
                print(content)
            elif read_mode == 'line':
                for line in file:
                    print(line, end='')
            else:
                print("на выбор только full или line.")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")


print("Чтение всего файла:")
read_file('example.txt', 'full')
print("\nЧтение построчно:")
read_file('example.txt', 'line')

def write_to_file():
    user_input = input("Введите текст для записи в файл: ")

    with open('user_input.txt', 'w', encoding='utf-8') as file:
        file.write(user_input + '\n')
    print("готово.")

def append_to_file():
    user_input = input("введите текст для добавления в файл: ")

    with open('user_input.txt', 'a', encoding='utf-8') as file:
        file.write(user_input + '\n')

    print("готово.")

write_to_file()
append_to_file()

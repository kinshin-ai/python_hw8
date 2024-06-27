class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, surname, name, patronymic, phone_number):
        contact = {
            'surname': surname,
            'name': name,
            'patronymic': patronymic,
            'phone_number': phone_number
        }
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Телефонная книга пуста.")
        else:
            for contact in self.contacts:
                print(f"{contact['surname']} {contact['name']} {contact['patronymic']} - {contact['phone_number']}")

    def import_contacts(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    surname, name, patronymic, phone_number = line.strip().split(', ')
                    self.add_contact(surname, name, patronymic, phone_number)
            print("Контакты успешно импортированы.")
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def export_contacts(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for contact in self.contacts:
                    line = f"{contact['surname']}, {contact['name']}, {contact['patronymic']}, {contact['phone_number']}\n"
                    file.write(line)
            print("Контакты успешно экспортированы.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query in contact.values()]
        if results:
            for contact in results:
                print(f"{contact['surname']} {contact['name']} {contact['patronymic']} - {contact['phone_number']}")
            return results
        else:
            print("Контакт не найден.")
            return []

    def edit_contact(self, query):
        results = self.search_contacts(query)
        if results:
            contact = results[0]
            print("Редактируем контакт: ")
            self.display_contact(contact)
            surname = input("Введите новую фамилию (оставьте пустым для пропуска): ")
            name = input("Введите новое имя (оставьте пустым для пропуска): ")
            patronymic = input("Введите новое отчество (оставьте пустым для пропуска): ")
            phone_number = input("Введите новый номер телефона (оставьте пустым для пропуска): ")

            if surname:
                contact['surname'] = surname
            if name:
                contact['name'] = name
            if patronymic:
                contact['patronymic'] = patronymic
            if phone_number:
                contact['phone_number'] = phone_number
            print("Контакт обновлен.")
        else:
            print("Контакт не найден.")

    def delete_contact(self, query):
        results = self.search_contacts(query)
        if results:
            contact = results[0]
            self.contacts.remove(contact)
            print("Контакт удален.")
        else:
            print("Контакт не найден.")

    def display_contact(self, contact):
        print(f"{contact['surname']} {contact['name']} {contact['patronymic']} - {contact['phone_number']}")

def main():
    phone_book = PhoneBook()

    while True:
        print("\n1. Добавить контакт")
        print("\n2. Показать все контакты")
        print("\n3. Импортировать контакты из файла")
        print("\n4. Экспортировать контакты в файл")
        print("\n5. Поиск контакта")
        print("\n6. Редактировать контакт")
        print("\n7. Удалить контакт")
        print("\n8. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            phone_book.add_contact(surname, name, patronymic, phone_number)
        elif choice == '2':
            phone_book.display_contacts()
        elif choice == '3':
            file_path = input("Введите путь к файлу: ")
            phone_book.import_contacts(file_path)
        elif choice == '4':
            file_path = input("Введите путь к файлу: ")
            phone_book.export_contacts(file_path)
        elif choice == '5':
            query = input("Введите имя, фамилию или отчество для поиска: ")
            phone_book.search_contacts(query)
        elif choice == '6':
            query = input("Введите имя, фамилию или отчество для редактирования: ")
            phone_book.edit_contact(query)
        elif choice == '7':
            query = input("Введите имя, фамилию или отчество для удаления: ")
            phone_book.delete_contact(query)
        elif choice == '8':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

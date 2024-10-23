class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id       # Инкапсулированный уникальный идентификатор
        self.__name = name             # Инкапсулированное имя
        self.__access_level = access_level  # Инкапсулированный уровень доступа (по умолчанию 'user')

    # Методы для получения данных пользователя
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Метод для изменения уровня доступа
    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level
        else:
            print("Некорректный уровень доступа.")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')  # Наследуем все от User, но с уровнем 'admin'

    def add_user(self, user_list, user):
        """Добавление нового пользователя в систему."""
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Неверный объект пользователя.")

    def remove_user(self, user_list, user_id):
        """Удаление пользователя из системы по ID."""
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удалён.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

# Пример использования системы управления пользователями
if __name__ == "__main__":
    # Создание списка пользователей
    user_list = []

    # Создание обычных пользователей
    user1 = User(1, "Алексей")
    user2 = User(2, "Мария")

    # Создание администратора
    admin = Admin(0, "Администратор")

    # Администратор добавляет пользователей в систему
    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)

    # Печатаем список всех пользователей
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 1)

    # Печатаем обновленный список пользователей
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

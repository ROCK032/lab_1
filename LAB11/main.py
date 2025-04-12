import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="phonebook_update",
        user="postgres",
        password="X6temax6",
        host="localhost",
        port="5432"
    )

def input_phone():
    while True:
        phone = input("Введите номер телефона (11 символов, начинается с 8): ")
        if len(phone) != 11:
            print("Ошибка: номер должен быть длиной 11 символов.")
        elif not phone.startswith('8'):
            print("Ошибка: номер должен начинаться с 8.")
        else:
            return phone

def add_user():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input_phone()

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO contacts (name, surname, phone_number) VALUES (%s, %s, %s)", (name, surname, phone))
        conn.commit()
        print("Пользователь добавлен!")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Ошибка: номер уже существует.")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

def update_user():
    print("Найти пользователя для обновления:")
    method = input("1 — по имени и фамилии\n2 — по номеру телефона\nВыберите: ")

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if method == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            cur.execute("SELECT * FROM contacts WHERE name = %s AND surname = %s", (name, surname))
            user = cur.fetchone()
            if not user:
                print("Пользователь не найден.")
                return
        elif method == '2':
            phone = input("Введите номер: ")
            cur.execute("SELECT * FROM contacts WHERE phone_number = %s", (phone,))
            user = cur.fetchone()
            if not user:
                print("Пользователь не найден.")
                return
        else:
            print("Неверный выбор")
            return

        print("\nЧто хотите обновить?")
        print("1 — Имя")
        print("2 — Фамилию")
        print("3 — Номер телефона")
        print("4 — Всё")

        choice = input("Выберите: ")

        if choice == '1':
            new_name = input("Введите новое имя: ")
            cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, user[0]))
        elif choice == '2':
            new_surname = input("Введите новую фамилию: ")
            cur.execute("UPDATE contacts SET surname = %s WHERE id = %s", (new_surname, user[0]))
        elif choice == '3':
            new_phone = input_phone()
            cur.execute("UPDATE contacts SET phone_number = %s WHERE id = %s", (new_phone, user[0]))
        elif choice == '4':
            new_name = input("Введите новое имя: ")
            new_surname = input("Введите новую фамилию: ")
            new_phone = input_phone()
            cur.execute(
                "UPDATE contacts SET name = %s, surname = %s, phone_number = %s WHERE id = %s",
                (new_name, new_surname, new_phone, user[0])
            )
        else:
            print("Неверный выбор.")
            return

        conn.commit()
        print("Пользователь успешно обновлён.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Ошибка: такой номер уже существует.")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

def delete_user():
    print("Удалить пользователя:")
    method = input("1 — по имени и фамилии\n2 — по номеру телефона\nВыберите: ")

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if method == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            cur.execute("DELETE FROM contacts WHERE name = %s AND surname = %s", (name, surname))
        elif method == '2':
            phone = input("Введите номер: ")
            cur.execute("DELETE FROM contacts WHERE phone_number = %s", (phone,))
        else:
            print("Неверный выбор")
            return

        if cur.rowcount == 0:
            print("Пользователь не найден.")
        else:
            conn.commit()
            print("Пользователь удалён.")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

def find_user():
    print("Найти пользователя:")
    method = input("1 — по имени и фамилии\n2 — по номеру телефона\nВыберите: ")

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        if method == '1':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            cur.execute("SELECT * FROM contacts WHERE name = %s AND surname = %s", (name, surname))
        elif method == '2':
            phone = input("Введите номер: ")
            cur.execute("SELECT * FROM contacts WHERE phone_number = %s", (phone,))
        else:
            print("Неверный выбор")
            return

        rows = cur.fetchall()
        if not rows:
            print("Пользователь не найден.")
        else:
            for row in rows:
                print(f"{row[0]}. {row[1]} {row[2]} - {row[3]}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

def show_all():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        for row in rows:
            print(f"{row[0]}. {row[1]} {row[2]} - {row[3]}")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        cur.close()
        conn.close()

def main():
    while True:
        print("\n1. Добавить нового пользователя")
        print("2. Обновить номер пользователя")
        print("3. Удалить пользователя")
        print("4. Найти пользователя")
        print("5. Показать всех пользователей")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            update_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            find_user()
        elif choice == '5':
            show_all()
        elif choice == '6':
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
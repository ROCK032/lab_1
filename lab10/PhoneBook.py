import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="X6temax6",
        host="localhost",
        port="5432"
    )

def update_user():
    conn = get_db_connection()
    cur = conn.cursor()
    find_by = input("Найти по (1) имени или (2) телефону? ")
    if find_by == '1':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    elif find_by == '2':
        phone = input("Введите телефон: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", ('%' + phone + '%',))
    else:
        print("Неверный выбор.")
        return
    results = cur.fetchall()
    if not results:
        print("Пользователь не найден.")
        return
    for row in results:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    id_to_update = input("Введите ID пользователя для обновления: ")
    update_choice = input("Что изменить? (1) Имя, (2) Телефон, (3) Оба: ")
    if update_choice == '1':
        new_name = input("Новое имя: ")
        cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, id_to_update))
    elif update_choice == '2':
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, id_to_update))
    elif update_choice == '3':
        new_name = input("Новое имя: ")
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE contacts SET name = %s, phone = %s WHERE id = %s", (new_name, new_phone, id_to_update))
    else:
        print("Неверный выбор.")
        return
    conn.commit()
    print("Данные обновлены.")
    cur.close()
    conn.close()

def show_all_contacts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    cur.close()
    conn.close()

def search_user():
    conn = get_db_connection()
    cur = conn.cursor()
    search_by = input("Искать по (1) имени или (2) телефону? ")
    if search_by == '1':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    elif search_by == '2':
        phone = input("Введите телефон: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", ('%' + phone + '%',))
    else:
        print("Неверный выбор.")
        return
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
    else:
        print("Пользователь не найден.")
    cur.close()
    conn.close()

def delete_user():
    conn = get_db_connection()
    cur = conn.cursor()
    choice = input("Удалить по (1) имени или (2) телефону? ")
    if choice == '1':
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", ('%' + phone + '%',))
    else:
        print("Неверный выбор.")
        return
    users = cur.fetchall()
    if users:
        for user in users:
            print(f"ID: {user[0]} | Имя: {user[1]} | Телефон: {user[2]}")
        confirm = input("Удалить эти записи? (да/нет): ")
        if confirm.lower() == "да":
            if choice == '1':
                cur.execute("DELETE FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
            else:
                cur.execute("DELETE FROM contacts WHERE phone LIKE %s", ('%' + phone + '%',))
            conn.commit()
            print("Удалено.")
        else:
            print("Отменено.")
    else:
        print("Пользователь не найден.")
    cur.close()
    conn.close()

def add_user():
    conn = get_db_connection()
    cur = conn.cursor()
    name = input("Введите имя: ").strip()
    phone = input("Введите номер: ").strip()
    if not name or not phone:
        print("Имя и номер не должны быть пустыми.")
        return
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Пользователь добавлен.")
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n1. Обновить данные")
        print("2. Вывести все данные")
        print("3. Поиск по имени или телефону")
        print("4. Удалить данные по имени или телефону")
        print("5. Добавить нового пользователя")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            update_user()
        elif choice == '2':
            show_all_contacts()
        elif choice == '3':
            search_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            add_user()
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

menu()

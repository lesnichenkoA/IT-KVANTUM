import sqlite3


def insert_varible_into_table(user_id, name, number, mail):
    try:
        sqlite_connection = sqlite3.connect('main_db.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_with_param = """INSERT INTO users
                              (user_id, name, number, mail)
                              VALUES (?, ?, ?, ?);"""

        data_tuple = (user_id, name, number, mail)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

import psycopg2
from psycopg2 import Error
import csv
from lib_gz import *

try:
    # Подключиться базе данных gz
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    if table_exist(cursor, 'products'):
        # Удаляем записи с таблицы
        cursor.execute("DELETE FROM products;")
        connection.commit()
    else:
        # Создаем таблицу products
        create_table = """CREATE TABLE IF NOT EXISTS products (
            sname VARCHAR(50),
            name VARCHAR(2000),
            name_dop VARCHAR(500),
            qty REAL,
            unit VARCHAR(30),
            price REAL,
            total REAL,
            contract VARCHAR(30),
            year INTEGER,
            customer VARCHAR(500),
            ftext VARCHAR(30)
        );"""
        cursor.execute(create_table)
        connection.commit()
        print('Таблица products успешно создана в PostgreSQL')

    # Заполняем таблицу products из одноименного csv файла
    convert_ods_to_csv('products.csv')
    with open(path_to_data + 'products.csv', 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        num = 1
        for row in reader:
            if len(row['sname']) > 0:
                print('Обработка строки - ', num)
                num += 1
                qty = replace_comma_to_dot(row['qty'])
                price = replace_comma_to_dot(row['price'])
                total = replace_comma_to_dot(row['total'])
                # Выполнение SQL-запроса для вставки данных в таблицу
                insert_query = f"""
                    INSERT INTO products (sname, name, name_dop, qty, unit, price, total, contract, year, customer, ftext)
                    VALUES ('{row['sname']}', '{row['name']}', '{row['name_dop']}', '{qty}', '{row['unit']}', '{price}', 
                    '{total}', '{row['contract']}', '{row['year']}', '{row['customer']}', '{row['ftext']}');
                """
                cursor.execute(insert_query)
                connection.commit()

except (Exception, Error) as error:
    print('Ошибка при работе с PostgreSQL', error)
finally:
    if connection:
        cursor.close()
        connection.close()

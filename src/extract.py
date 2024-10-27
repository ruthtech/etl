import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import errorcode
import numpy as np
import os
import pandas as pd
import yaml


def load_csv(csv_directory):
    try:
        for files in os.listdir(csv_directory):
            if files.endswith('.csv'):
                books = pd.read_csv(os.path.join(csv_directory,
                                                 files))  # If the values in the CSV file contain commas, then it must be enclosed inside double quotes.
                df = pd.DataFrame(books)
                print(df)

    except FileNotFoundError:
        print(f'Directory must exist {csv_directory}')


def mysql_connect():
    db = yaml.safe_load(open('db.yaml'))
    config = {
        'user': db['user'],
        'password': db['password'],
        'host': db['host'],
        'database': db['db'],
        'auth_plugin': 'mysql_native_password'
    }
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database must exist.")
        else:
            print(err)


def mysql_close(cnx, cursor):
    if cursor is not None:
        cursor.close()
    if cnx is not None:
        cnx.close()


def execute(cursor, statements):
    for statement in statements:
        cursor.execute(statement)
        rows = cursor.fetchall()

        print(f'Result for statement {statement}:')
        for row in rows:
            print(f'{row}')
        print('\n')


def main():
    csv_directory = '../data/tests/'
    load_csv(csv_directory)

    cnx, cursor = mysql_connect()

    statements = [
        'SHOW DATABASES;',
        'USE `education`;',
        'CREATE TABLE `books` (`ISBN` bigint NOT NULL, `author_last_name` varchar (20) NOT NULL, `author_initials` varchar(3) NOT NULL, `title` VARCHAR(100) NOT NULL, `publisher` VARCHAR(50)) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;',
        'INSERT INTO `books` VALUES(9781732102200, "Ousterhout", "J", "A Philosophy Of Software Design", "Yaknyam Press");',
        'INSERT INTO `books` VALUES(9781098146962, "Yablonski", "J", "Laws of UX: Using Psychology To Design Better Products & Services", "O-Reilly Media, Inc.");',
        'INSERT INTO `books` VALUES(9780201563641, "Meyers", "S", "Effective C++", "Addison-Wesley");',
        'INSERT INTO `books` VALUES(9780201889543, "Stroustrup", "B", "The C++ Programming Language", "AT & T");',
        'SELECT * FROM `books`;',
        'DROP TABLE `books`;'
    ]
    execute(cursor, statements)

    mysql_close(cnx, cursor)


main()

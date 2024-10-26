import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import errorcode
import os
import yaml

db = yaml.safe_load(open('db.yaml'))
config = {
    'user': db['user'],
    'password': db['password'],
    'host': db['host'],
    'database': db['db'],
    'auth_plugin': 'mysql_native_password'
}
cnx = mysql.connector.connect(**config)

import mysql.connector
from mysql.connector import errorcode


def execute(statements):
    config = {
        'user': 'user',
        'password': 'password',
        'host': '127.0.0.1',
        'raise_on_warnings': True
    }
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        for statement in statements:
            cursor.execute(statement)
            rows = cursor.fetchall()

            print(f'Result for statement {statement}:')
            for row in rows:
                print(f'{row}')
            print('\n')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database must exist.")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()


def main():
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
    execute(statements)


main()

# sql = ("""
# SELECT
#   DATE_FORMAT(date, '%d-%m-%Y'),
#   CAST(sum(sales) as UNSIGNED) as sales
# FROM mrts
# WHERE
#   kind = 'Retail and food services sales, total'
# GROUP BY 1
# """
#
#        cursor.execute(sql)
# month = []
# sales = []
#
# # print all the first cell of all the rows
# for row in cursor.fetchall():
#     print(row)
# month.append(row[0])
# sales.append(row[1])
#
# cursor.close()
# cnx.close()
#
# plt.plot(month, sales)
# plt.show()

import psycopg2
import csv
from config import load_config

csv_file_path = r"C:\Users\user\Desktop\kbtu\university pp\PP2\week10\pb.csv"


def create_tables():
    commands = (
        """
        CREATE TABLE phonebook (
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(100) NOT NULL,
            phone_number VARCHAR(15) NOT NULL
        )""",
    )

    try:

        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


#
def insert_csv():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(csv_file_path, 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)",(row[0], row[1]))
                conn.commit()
                print("data inserted")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
#console input
def insert_console():
    user_name = input("name: ")
    phone_number = input("phone number: ")

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phonebook (user_name, phone_number) VALUES (%s,%s)", (user_name, phone_number))
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
    insert_csv()
    insert_console()


#update!!

'''
def update_data():
    choice = input("change number or name?: ")
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if choice == "name":
                    old_name = input("which name to change?: ")
                    new_name = input("new name: ")
                    cur.execute("UPDATE phonebook SET user_name = %s WHERE user_name = %s", (new_name, old_name))
                    print("name updated.")

                if choice == "phone":
                    user = input("user name: ")
                    new_phone = input("new phone number: ")
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE user_name = %s", (new_phone, user))
                    print("phone number updated")
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    update_data()
'''
#deletes data
'''
def delete(user):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE user_name = %s", (user,))
    except ( Exception, psycopg2.DatabaseError) as error:
        print(error)
    print(f"{user} deleted")

if __name__ == '__main__':
    user = input("user to delete: ")
    delete(user)
               
'''

'''
def query():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, user_name FROM phonebook ORDER BY user_name")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    query()
'''
    
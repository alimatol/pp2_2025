import psycopg2
from config import load_config



def user_score():
    commands = (
        """
        CREATE TABLE table_snake(
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            score INT NOT NULL,
            level INT NOT NULL
        )""",
    )

    try:

        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_scores(username, score, level):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO table_snake (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
                print("data inserted")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    user_score()



import psycopg2

class DatabaseConnection:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(dbname = 'codjoe', user = 'codjoe', 
            password = 'newpassword', host = 'localhost', port = '5432')
            self.cursor = self.conn.cursor()
            self.conn.autocommit = True
            print('\n\nDatabase connect success\n\n')
        except Exception as e:
            print(e)
            print('\n\nDatabase connect fail\n\n')

        
    def create_users_table(self):
        users_table = """ CREATE TABLE users (
                            user_id SERIAL PRIMARY KEY,
                            first_name VARCHAR(15) NOT NULL,
                            last_name VARCHAR(15) NOT NULL,
                            age INT NOT NULL,
                            email CHAR(25) NOT NULL,
                            password VARCHAR(25) NOT NULL,
                            created_at DATE NOT NULL DEFAULT CURRENT_DATE 
                            )"""

        self.cursor.execute(users_table)
        self.conn.close()

        return "Table create success"


    def create_category_table(self):
        tasks_table = """ CREATE TABLE categories (
                            category_id SERIAL PRIMARY,
                            category_name VARCHAR(15),
                            title VARCHAR(15),
                            description CHAR(80),
                            created_at DATE NOT NULL DEFAULT CURRENT_DATE
                            )"""

        self.cursor.execute(tasks_table)
        self.conn.close()

        return "Table create success"
    

    def create_tasks_table(self):
        tasks_table = """ CREATE TABLE tasks (
                            task_id SERIAL PRIMARY KEY,
                            user_id INT references users(user_id),
                            category_id INT references categories(category_id),
                            title VARCHAR(15) NOT NULL,
                            description CHAR(80) NOT NULL,
                            done VARCHAR(5),
                            created_at DATE NOT NULL DEFAULT CURRENT_DATE 
                            )"""

        self.cursor.execute(tasks_table)
        self.conn.close()

        return "Table create success"
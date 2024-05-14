import mysql.connector
import datetime


# создаем БД
def create_db():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="user",
        passwd="12345",
        database="database"

    )

    mycursor = dataBase.cursor()

    mycursor.execute('''
    CREATE TABLE IF NOT EXISTS info_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        api_url VARCHAR(255),
        success INT,
        success_result VARCHAR(1000) DEFAULT NULL,
        error VARCHAR(500) DEFAULT NULL
    )
    ''')

    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS result (
            id INT AUTO_INCREMENT PRIMARY KEY,
            api_url VARCHAR(255),
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            processing_time INT,
            success INT,
            series VARCHAR(20),
            number VARCHAR(30),
            department VARCHAR(200),
            code VARCHAR(15),
            date_of_issue VARCHAR(30),
            gender VARCHAR(10),
            birthplace VARCHAR(150),
            last_name VARCHAR(100),
            first_name VARCHAR(100),
            patronymic VARCHAR(100),
            bdate VARCHAR(15),
            type_doc VARCHAR(30)
        )
        ''')



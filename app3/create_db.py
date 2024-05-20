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
    CREATE TABLE IF NOT EXISTS data_passport (
        id INT AUTO_INCREMENT PRIMARY KEY,
        deregistered_name_departament VARCHAR(300) DEFAULT NULL,
        deregistered_code_departament VARCHAR(15) DEFAULT NULL,
        deregistered_date DATE DEFAULT NULL,
        registered_house VARCHAR(20) DEFAULT NULL,
        registered_name_departament VARCHAR(300) DEFAULT NULL,
        registered_district VARCHAR(300) DEFAULT NULL,
        registered_code_departament VARCHAR(15) DEFAULT NULL,
        registered_date DATE DEFAULT NULL,
        registered_station VARCHAR(300) DEFAULT NULL,
        registered_region VARCHAR(300) DEFAULT NULL,
        registered_street VARCHAR(300) DEFAULT NULL,
        success TINYINT DEFAULT NULL,
        processing_time INT DEFAULT NULL
    )
    ''')

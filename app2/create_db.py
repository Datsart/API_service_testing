import mysql.connector

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

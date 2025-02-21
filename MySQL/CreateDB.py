import mysql

config = {
    'user':'root',
    'password': 'root',
    'host': 'localhost',
    'port' : 3306
}

with mysql.connector.connect(**config) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("SHOW DATABASES;")
        dbs = [db[0] for db in cursor]
        if not any(map(lambda n : n == "Weather", dbs)):
            cursor.execute("CREATE DATABASE Weather;")
            print("The database 'Weather' was created succesfully!")
        else:
            print("The database 'Weather' already exists!")
    cnx.commit()

with mysql.connector.connect(database='Weather', **config) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS WeatherData(
                )
            """)

if __name__ == '__main__':
    print("The database and table were created succesfully!")
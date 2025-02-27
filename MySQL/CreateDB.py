import mysql.connector, subprocess

config : dict = {
    'user':'root',
    'password': 'root',
    'host': 'localhost',
    'port' : 3306
}

database : bool = None
table : bool = None

with mysql.connector.connect(**config) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("SHOW DATABASES;")
        dbs : list = [db[0] for db in cursor]
        if not any(map(lambda n : n == "Weather", dbs)):
            database = True
            cursor.execute("CREATE DATABASE Weather;")
            # print("The database 'Weather' was created succesfully!")
        else:
            database = False
            # print("The database 'Weather' already exists!")
    cnx.commit()

with mysql.connector.connect(database='Weather', **config) as cnx:
    with cnx.cursor() as cursor:
        cursor.execute("SHOW TABLES;")

        tables : list = [table[0] for table in cursor]
        if not any(map(lambda n : n == "WeatherData", tables)):
            table = True
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS WeatherData(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Temperature_C FLOAT NOT NULL,
                    Pressure FLOAT NOT NULL,
                    Humidity FLOAT NOT NULL,
                    UVI FLOAT NOT NULL,
                    Visibility FLOAT NOT NULL,
                    WindSpeed FLOAT NOT NULL,
                    WindDegree FLOAT NOT NULL
                    );
                """)
        else:
            table = False
            # print("The table 'WeatherData' already exists!")
        cnx.commit()


if __name__ == "__main__":
    print(f"\n")
    if database and table:
        print("The database and table were created succesfully!")
    elif database and not table:
        print("The database was created succesfully, but the table already exists!")
    elif not database and table:
        print("The database already exists, but the table was created succesfully!")
    else:
        print("The database and table already exist!")

    look_inside = input("Do you want to see the databases and tables? [db/tab/both] : ")

    if look_inside == "db":
        print(f"\nHere's the list of databases : ")
        print("Introduce the password for 'root' user when prompted.")
        subprocess.run("mysql -u root -p --execute 'SHOW DATABASES;'", shell = True)
    elif look_inside == "tab":
        print(f"\n")
        print("Here's the list of columms of the table 'WeatherData' : ")
        print("Introduce the password for 'root' when prompted.")
        subprocess.run("mysql -u root -p --execute 'SHOW COLUMNS FROM Weather.WeatherData;'", shell = True)
    elif look_inside == "both":
        print(f"\nHere's the list of databases : ")
        print("Introduce the password for 'root' user when prompted.")
        subprocess.run("mysql -u root -p --execute 'SHOW DATABASES;'", shell = True)

        print(f"\n")
        print("Here's the list of columms of the table 'WeatherData' : ")
        print("Introduce the password 'root' when prompted.")
        subprocess.run("mysql -u root -p --execute 'SHOW COLUMNS FROM Weather.WeatherData;'", shell = True)

    print(f"\nBye!\n")
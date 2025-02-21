CREATE DATABASE IF NOT EXISTS Weather;

USE Weather;

CREATE TABLE IF NOT EXISTS WeatherData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    wind_direction FLOAT NOT NULL,
    weather VARCHAR(255) NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

SELECT "Done!, you've created the database and table successfully!" AS MESSAGE;
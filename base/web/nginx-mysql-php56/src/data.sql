CREATE DATABASE IF NOT EXISTS cssec;

USE cssec;

CREATE TABLE IF NOT EXISTS flag (
    flag VARCHAR(255) NOT NULL
);

INSERT INTO flag (flag) VALUES ('flag{seek_to_geek}');
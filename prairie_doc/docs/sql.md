# SQL

Quelques notions de SQL


```sql

INSERT INTO city (name, lat,lon)
 VALUES (' Montcuq', 510614,  1926438)
 INSERT INTO people (name, height,date_of_birth, place_of_birth)
 VALUES (' Manon', 10000, 19/05/1920, "berk")
 
 INSERT INTO people (name, height, date_of_birth, place_of_birth) VALUES
('Alice', 170, '1990-01-15', 'Paris'),
('Bob', 180, '1985-05-23', 'Lyon'),
('Charlie', 175, '1992-03-10', 'Marseille'),
('Diane', 165, '1988-07-19', 'Toulouse'),
('Emma', 160, '1995-11-02', 'Nice'),
('Farid', 182, '1991-08-30', 'Nantes'),
('Hugo', 178, '1989-04-12', 'Bordeaux'),
('Isabelle', 168, '1993-09-25', 'Lille'),
('Julien', 177, '1987-06-05', 'Strasbourg'),
('Karen', 164, '1994-12-18', 'Rennes'),
('Leo', 185, '1990-02-14', 'Montpellier'),
('Maya', 162, '1996-10-07', 'Dijon'),
('Nathan', 179, '1986-03-22', 'Reims'),
('Olivia', 167, '1992-05-17', 'Le Havre'),
('Paul', 180, '1988-09-30', 'Saint-Étienne'),
('Quentin', 176, '1991-07-11', 'Angers'),
('Roxane', 163, '1993-01-20', 'Grenoble'),
('Samuel', 183, '1989-11-29', 'Clermont-Ferrand'),
('Théo', 181, '1994-08-04', 'Tours'),
('Valérie', 165, '1995-06-15', 'Orléans');

SELECT * FROM tableau

SELECT name, date_of_birth
FROM people
ORDER BY date_of_birth

SELECT name, date_of_birth
FROM people
ORDER BY date_of_birth DESC

SELECT name, place_of_birth from people GROUP BY place_of_birth
```
1. exercise-01
Write a SQL query to select the sex and body mass columns from the little_penguins in that order, 
sorted such that the largest body mass appears first.
SQL:
SELECT sex, body_mass_g
FROM penguins
ORDER BY body_mass_g DESC;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-1.png

2. exercise-02
Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.
Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.
SQL:
SELECT island,species FROM penguins
LIMIT 11 OFFSET 49;

SELECT DISTINCT island,species FROM penguins;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-2.png

3. exercise-03
Write a query to select the body masses from penguins that are less than 3000.0 grams.

Write another query to select the species and sex of penguins that weight less than 3000.0 grams. 
This shows that the columns displayed and those used in filtering are independent of each other.
SQL:
SELECT body_mass_g
FROM penguins
WHERE body_mass_g < 3000.0;

SELECT species, sex
FROM penguins
WHERE body_mass_g < 3000.0;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-3.png

4. exercise-04
Use the not operator to select penguins that are not Gentoos.

SQL's or is an inclusive or: it succeeds if either or both conditions are true. 
SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, 
but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on 
Torgersen Island but not both.
SQL:
SELECT *
FROM penguins
WHERE NOT species = 'Gentoo'

SELECT *
FROM penguins
WHERE (sex = 'female' OR island = 'Torgersen')
AND NOT (sex = 'female' AND island = 'Torgersen');

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-4.png

5. exercise-05
Write a single query that calculates and returns:

A column called what_where that has the species and island of each penguin separated by a single space.
A column called bill_ratio that has the ratio of bill length to bill depth.
You can use the || operator to concatenate text to solve part 1, or look at the documentation for SQLite's format() function.
SQL:
SELECT 
    species || ' ' || island AS what_where,
    bill_length_mm / bill_depth_mm AS bill_ratio
FROM penguins;


Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-5.png

6. exercise-06
Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?
SQL:
.nullvalue null
SELECT 
    species || ' ' || island AS what_where,
    bill_length_mm / bill_depth_mm AS bill_ratio
FROM penguins;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-6.png

7. exercise-07
Write a query to find penguins whose body mass is known but whose sex is not.

Write another query to find penguins whose sex is known but whose body mass is not.
SQL:
SELECT *
FROM penguins
WHERE body_mass_g IS NOT NULL
AND sex IS NULL;

SELECT *
FROM penguins
WHERE sex IS NOT NULL
AND body_mass_g IS NULL;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-7.png

8. exercise-08
What is the average body mass of penguins that weight more than 3000.0 grams
SQL:
SELECT AVG(body_mass_g) AS average_body_mass_g
FROM penguins
WHERE body_mass_g > 3000.0;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-8.png

9. exercise-09
How many different body masses are in the penguins dataset?
SQL:
SELECT COUNT(DISTINCT body_mass_g) AS distinct_body_mass_count
FROM penguins;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-9.png

10. exercise-10
Explain why the output of the previous query has a blank line before the rows for female and male penguins.

Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much.
SQL:
SELECT 
    body_mass_g, 
    COUNT(*) AS penguin_count
FROM penguins
GROUP BY body_mass_g;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-10.png

11. exercise-11
Write a query that uses filter to calculate the average body masses of heavy penguins 
(those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. 
Is it possible to do this using where instead of filter?
SQL:
SELECT 
    AVG(body_mass_g) FILTER (WHERE body_mass_g > 4500) AS avg_heavy_penguins,
    AVG(body_mass_g) FILTER (WHERE body_mass_g < 3500) AS avg_light_penguins
FROM penguins;

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-11.png

12. exercise-12
Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. Use a query to check that the notes have been stored and that you can (for example) select by author name.

What happens if you try to insert too many or too few values into notes? What happens if you insert a number instead of a string into the note field?
SQL:
CREATE TABLE notes (
    author TEXT,
    note TEXT
);
INSERT INTO notes (author, note) VALUES ("Duad", "Commit suicide."),
("Hadan", "Deez nuts."), ("Candice", "Who's candice."), ("Andy", "Everything is dandy.")

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-12.png

13. exercise-13
What happens if you try to delete rows that don't exist (e.g., all entries in work that refer to juna)?
SQL:
DELETE FROM notes WHERE author = 'Joe';

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-13.png

14. exercise-14
Saving and restoring data as text:

Re-create the notes table in an in-memory database and then use SQLite's .output and .dump commands to save the database to a file called notes.sql. 
Inspect the contents of this file: how has your data been stored?

Start a fresh SQLite session and load notes.sql using the .read command. Inspect the database using .schema and select *: is everything as you expected?

Saving and restoring data in binary format:

Re-create the notes table in an in-memory database once again and use SQLite's .backup command to save it to a file called notes.db. 
Inspect this file using od -c notes.db or a text editor that can handle binary data: how has your data been stored?

Start a fresh SQLite session and load notes.db using the .restore command. Inspect the database using .schema and select *: is everything as you expected?
SQL:
.output notes.sql
.dump
.output stdout
.read notes.sql

.backup notes.db
.restore notes.db

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-14.png

15. exercise-15

Find the least time each person spent on any job. Your output should show that mik and po each spent 0.5 hours on some job. Can you find a way to show the name of the job as well using the SQL you have seen so far?
SQL:
SELECT work.person, work.job, work.hours
FROM work
WHERE work.hours = (
    SELECT MIN(w.hours)
    FROM work AS w
    WHERE w.person = work.person
);

Screenshot: https://github.com/JajoKS/ISI_AMW_KS/blob/main/sql-exercises/screenshots/Ex-15.png
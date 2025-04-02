1. exercise-01
Write a SQL query to select the sex and body mass columns from the little_penguins in that order, 
sorted such that the largest body mass appears first.

Screenshot: 

2. exercise-02
Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.
Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.

Screenshot: 

3. exercise-03
Write a query to select the body masses from penguins that are less than 3000.0 grams.

Write another query to select the species and sex of penguins that weight less than 3000.0 grams. 
This shows that the columns displayed and those used in filtering are independent of each other.

Screenshot: 

4. exercise-04
Use the not operator to select penguins that are not Gentoos.

SQL's or is an inclusive or: it succeeds if either or both conditions are true. 
SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, 
but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on 
Torgersen Island but not both.

Screenshot: 

5. exercise-05
Write a single query that calculates and returns:

A column called what_where that has the species and island of each penguin separated by a single space.
A column called bill_ratio that has the ratio of bill length to bill depth.
You can use the || operator to concatenate text to solve part 1, or look at the documentation for SQLite's format() function.

Screenshot: 

6. exercise-06
Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?

Screenshot:

7. exercise-07
Write a query to find penguins whose body mass is known but whose sex is not.

Write another query to find penguins whose sex is known but whose body mass is not.

Screenshot:

8. exercise-08
What is the average body mass of penguins that weight more than 3000.0 grams

Screenshot:

9. exercise-09
How many different body masses are in the penguins dataset?

Screenshot:

10. exercise-10
Explain why the output of the previous query has a blank line before the rows for female and male penguins.

Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much.

Screenshot:

11. exercise-11
Write a query that uses filter to calculate the average body masses of heavy penguins 
(those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. 
Is it possible to do this using where instead of filter?

Screenshot:

12. exercise-12
Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. Use a query to check that the notes have been stored and that you can (for example) select by author name.

What happens if you try to insert too many or too few values into notes? What happens if you insert a number instead of a string into the note field?

Screenshot:
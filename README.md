## SQL - Working with Data 

To Create a Database 
    >  CREATE DATABASE database_name;

To Use a Database 
    > USE database_name;

To create a Table
    > create table table_name (column_1 datatype size, .,.,.,.,);

To insert data into a table
    > insert into table_name values 
    (),();

To insert data into specific columns of table 
    > insert into table_name column_name(s)  values ();


> Example:

    DROP TABLE IF EXISTS `offices`;

    CREATE TABLE `offices` (
    `officeCode` varchar(10) NOT NULL,
    `city` varchar(50) NOT NULL,
    `phone` varchar(50) NOT NULL,
    `addressLine1` varchar(50) NOT NULL,
    `addressLine2` varchar(50),
    `state` varchar(50),
    `country` varchar(50) NOT NULL,
    `postalCode` varchar(15) NOT NULL,
    `territory` varchar(10) NOT NULL,
    PRIMARY KEY (`officeCode`)
    );


> Primary Key uniquely identifies each record in a table, Must contain   unique values and cannot be null. A table can only have one Primary key, This can consist of single or multiple columns.

Viewing Data: The simplest way to view data from the table is using the SELECT statement. It has the following syntax:

    SELECT column1, column2, ... FROM table_name;
    You can also view data from all columns using

    SELECT * FROM `offices`;


#### Querying with WHERE
    ``We can add a WHERE clause to a SELECT statement to select just the rows satisfying the given clause. Here's an example:

    SELECT * FROM `employees` WHERE `jobTitle`="Sales Rep";
    Note that values with spaces must be placed within quotes e.g. "Sales Rep".

    The WHERE clause supports the following operators:

    =
    >
    <
    >=
    <=
    <> or !=
    BETWEEN
    LIKE
    IN
    Expressions within a WHERE clause can be combined using AND and OR.

    SELECT column1, column2, ...
    FROM table_name
    WHERE condition1 AND condition2 AND condition3 ...;
    An expression within a WHERE clause can be negated using NOT.``

SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
> You can use a WHERE clause with SELECT, UPDATE, and DELETE statements


# SQL Introduction

## Resources

Read or watch:

- [What is Database & SQL?](https://www.digitalocean.com/community/tutorials/what-is-database-sql)
- [Install MySQL (MySQL Server)](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)
- [A Basic MySQL Tutorial](https://www.mysqltutorial.org/)
- [Basic SQL statements: DDL and DML](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
- [Basic queries: SQL and RA](https://www.geeksforgeeks.org/sql-basic-queries/)
- [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
- [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- Due to a temporary bug with some of the resources above, you can find most of the information [here](https://www.mysqltutorial.org/).

## Learning Objectives

At the end of this project, you should be able to explain to anyone, without the help of Google:

### General

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file

Example:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Use the sandbox to run MySQL

#### For Ubuntu 22.04 (Current image on CoD Platform)

1. Ask for a container Ubuntu 22.04
2. Update package list:
    ```bash
    apt update
    ```
3. Install mysql-server package:
    ```bash
    apt install -y mysql-server
    ```
4. Check it was installed properly:
    ```bash
    mysql --version
    # mysql  Ver 8.0.39-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
    ```
5. Start MySQL Server service:
    ```bash
    service mysql start
    ```
6. Connect to the server using the MySQL CLI:
    ```bash
    mysql -uroot
    ```

#### For Ubuntu 20.04 Sandbox (OLD IMAGE)

- In the container, credentials are `root/root`
- Start MySQL before using it:
    ```bash
    service mysql start
    ```
- Run SQL scripts:
    ```bash
    cat 0-list_databases.sql | mysql -uroot -p
    ```
- Example output:
    ```
    Database
    information_schema
    mysql
    performance_schema
    sys
    ```

#### Install MySQL 8.0 on Ubuntu 20.04 LTS

On your computer, VM, or WSL instance:

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
# mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

Connect to your MySQL server:

```bash
sudo mysql
```

Type `quit` to exit the MySQL monitor.

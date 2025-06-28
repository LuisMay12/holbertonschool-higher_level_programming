# SQL - More Queries

## Resources

Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html#sql-syntax-data-definition-constraints)
- [Basic query operation: the join](https://www.sqlshack.com/sql-join-types-with-examples/)
- [SQL technique: multiple joins and the distinct keyword](https://www.sqltutorial.org/sql-distinct/)
- [SQL technique: join types](https://www.sqltutorial.org/sql-join/)
- [SQL technique: subqueries](https://www.sqltutorial.org/sql-subquery/)
- [SQL technique: union and minus](https://www.sqltutorial.org/sql-union/)
- [MySQL Cheat Sheet](https://devhints.io/mysql)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/mysql-join.html)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax.html)

Extra resources around relational database model design:

- [Design](https://www.lucidchart.com/pages/er-diagrams)
- [Normalization](https://www.studytonight.com/dbms/database-normalization.php)
- [ER Modeling](https://www.lucidchart.com/pages/er-diagrams)

## Learning Objectives

At the end of this project, you should be able to explain, without external help:

### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (i.e. syntax above)
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.)
- A `README.md` file at the root of the project folder is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file

Example:
```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

> **Note:** If you’re using the provided sandbox you don’t need to install MySQL. Skip to the next section.

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

### Connect to your MySQL server

```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
...
mysql> quit
Bye
$
```

### Use the sandbox to run MySQL

- In the container, credentials are `root/root`
- Ask for container Ubuntu 20.04
- Connect via SSH or the Web terminal
- Start MySQL before using it:

```bash
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

### How to import a SQL dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
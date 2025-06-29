# Python Object Relational Mapping

## Before you start…
Please make sure your MySQL server is version **8.0**.  
See: [How to install MySQL 8.0 in Ubuntu 20.04](#install-mysql-80-on-ubuntu-2004-lts)

---

## Background Context

In this project, you will link two amazing worlds: **Databases** and **Python**!

- **Part 1:** Use the `MySQLdb` module to connect to a MySQL database and execute SQL queries.
- **Part 2:** Use the `SQLAlchemy` module (an Object Relational Mapper, ORM).

**The biggest difference:** No more SQL queries! ORMs abstract storage, letting you focus on objects, not storage details. Your code becomes storage-agnostic.

### Without ORM
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### With ORM
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

> The biggest difficulty with ORM is: **The syntax!**  
> Read tutorials as needed; don’t try to read the entire documentation before starting.

---

## Resources

Read or watch:

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.tutorialspoint.com/python/python_database_access.htm)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Introduction to SQLAlchemy](https://realpython.com/python-sqlalchemy/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://docs.sqlalchemy.org/en/14/faq/sessions.html)
- [Python SQLAlchemy Cheatsheet](https://cheatography.com/nikhilkumarsingh/cheat-sheets/sqlalchemy/)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) (uses PostgreSQL, but concepts are the same)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)

---

## Learning Objectives

By the end of this project, you should be able to explain:

- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (3.8.5)
- Use MySQLdb version 2.0.x and SQLAlchemy version 1.4.x
- All files should end with a new line
- First line of all files: `#!/usr/bin/python3`
- A `README.md` file at the root of the project is mandatory
- Code must use `pycodestyle` (2.7.*)
- All files must be executable
- File length will be tested using `wc`
- All modules, classes, and functions must have documentation
- Documentation must be a real sentence explaining the purpose
- **Do not use `execute` with SQLAlchemy**

---

## More Info

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```sh
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

#### Connect to your MySQL server:
```sh
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
...
mysql> quit
Bye
$
```

### Install MySQLdb module version 2.0.x
```sh
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
```sh
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

You may see this warning (can be ignored):
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")
  cursor.execute(statement, parameters)  
```
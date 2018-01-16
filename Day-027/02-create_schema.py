#!/usr/bin/env python3

import sqlite3
import os

sqlite3_db = "test.db"
sqlite3_schema = "test_schema.sql"

if os.path.exists(sqlite3_db):
    os.unlink(sqlite3_db)

with sqlite3.connect(sqlite3_db) as connection:
    print("Creating SQlite3 schema {}".format(sqlite3_schema))
    with open(sqlite3_schema) as schema_file:
        schema = schema_file.read()
    connection.executescript(schema)

    print("Adding initial data.")

    connection.executescript("""
        insert into project (subject, date, priority)
        values ("Testing sqlite3", "today", "high");
        """)

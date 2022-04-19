#!/usr/bin/env python3

import sqlite3
import os

import pathlib

sqlite3_db = "test.db"
sqlite3_schema = "test_schema.sql"

if os.path.exists(sqlite3_db):
    os.unlink(sqlite3_db)

with sqlite3.connect(sqlite3_db) as connection:
    print(f"Creating SQlite3 schema {sqlite3_schema}")
    schema = pathlib.Path(sqlite3_schema).read_text()
    connection.executescript(schema)

    print("Adding initial data.")

    connection.executescript(
        """
        insert into project (subject, date, priority)
        values ("Testing sqlite3", "today", "high");
        """
    )

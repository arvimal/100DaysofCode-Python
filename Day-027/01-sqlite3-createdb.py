#!/usr/bin/env python

import sqlite3
import os

sqlite3_db_name = "test.db"

db_connection = sqlite3.connect(sqlite3_db_name)
if os.path.exists(sqlite3_db_name):
    print("DB exists")
else:
    print("DB non-existent, needs creation.")
db_connection.close()

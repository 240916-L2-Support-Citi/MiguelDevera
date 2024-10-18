#!/usr/bin/python
# note: a proper cronjob for this looks like: * * * * * path_to_venv/<venv_name>/bin/python3 /<path_to_file>/alert_system.py
# psycopg2 is globally installed but we're using a venv

import psycopg
import Credentials
from GenerateMessage import generate_message
from EmailAlert import send_test_email
from FileAlert import write_alert_file

# Connect to the PostgreSQL database
db=Credentials.DB
table=Credentials.TABLE
pz=Credentials.PASSWORD_PC
userN=Credentials.USER

try:
    conn = psycopg.connect(
        dbname=db,
        user=userN,
        password=pz,
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()
    query = "select errorlevel, count(errorlevel) from {0} where errorlevel = '[ERROR]' or errorlevel = '[FATAL]' group by errorlevel order by errorlevel desc;".format(table)
    #should get something like:
    #  errorlevel | count
    # ------------+-------
    #  [FATAL]    |     1
    #  [ERROR]    |     5

    cursor.execute(query, prepare=True) #prepared statement
    tempf = cursor.fetchone()
    tempe = cursor.fetchone()
    fatal = 0
    error = 0
    if(tempf): #if no errors or fatals, we can't subscript so check first
        fatal = tempf[1]
    if(tempe):
        error = tempe[1]
    
    message = generate_message(fatal,error)
    print(message)
    write_alert_file(fatal,error)
    if(fatal >= 1 or error >= 5): # if we don't do this we'll get inane emails
        send_test_email(fatal,error)
except Exception as error1:
    print("Error with DB connection: ", error1)
finally:
    if conn:
        cursor.close()
        conn.close()
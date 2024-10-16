# Log Monitoring and Alert System - P1

## Description

In this project, I built a log monitoring and alert system using Bash, PostgreSQL, and Python. The system will monitor logs, store them in PostgreSQL, and trigger alerts when error thresholds are reached. This project aims to simulate real-world production support tasks.

## Goals

- Monitor log files for specific error levels (ERROR, FATAL).
- Insert log entries into a PostgreSQL database.
- Implement a Python-based alert system that tracks error thresholds.
- Create an automated email alert
- Automate scripts with cron jobs.

## How to Run

- A python virtual environment is recommended due to the use of psycopg
- Set up a psql db and user - then use the DDL to set up a table
- Use generate_logs.sh to make logs for the project (1)
- Run log_monitor.sh to filter logs into the psql db (2)
- Optional: automate log_monitor.sh using cron
- Run alert_system.py to see the status of the psql db - this may send an email, a console message, and create a file (3)
- Number of terminals: 2 - 3

### Calibration

- A virtual python env is recommended due to some dependancies
- Credentials.py requires actual data to be put in
- This project has all files contained within the same directory for ease of use. As such, it uses "./" as the file path for many things.
- The email you use in Credential.py to send may require an app-password (gmail)

## Files Explained

### Python: alert_system.py

- The major script that is ran to check the DB if the error and fatal threshold is met.
- Sends a console alert, an email alert, and writes to an alert file to update the status, even if the threshold is not met.
- the name is not camel case because that is what the project specs required at the time

### Python: Credentials.py

- Stores constants used for operating the scripts. When this is pushed, these will contain dummy data so as to maintain my privacy.
- SENDER: the email sender and the one you must log in to
- RECEIVER: the email reciever, no log in required
- PASSWORD_E: password for email
- PASSWORD_PC: password for your pc - note that my psql and my system password are the same and the files carry this assumption for you as well
- USER: username for your cmd and for psql - just like with PASSWORD_PC I use the same user for both system and psql
- FATAL: the fatal threshold, set to 1 for the project
- ERROR: the error threshold, set to 5 for the project
- DB: database name
- TABLE: table name - mind the use of schemas

### Python EmailAlert.py

- Uses smtplib and MIME to send out emails using the gmail server

### Python FileAlert.py

- Writes to a file (alert.txt) regarding the current status

### Python GenerateMessage.py

- Contains the generate_message() function, which is used by alert_system.py, EmailAlert.py, and FileAlert.py

### Bash generate_logs.sh

- An automated bash script meant to generate the log information used in this project

### Bash log_monitor.sh

- A bash script that reads from the log file (app.log) and filters ERROR and FATAL logs into the psql DB

### PSQL p1Setup.ddl

- A series of commands that creates the table and schema used for this project
- Does not create the DB or user, however - that must be done separately

## Technologies

- **Bash** for scripting.
- **PostgreSQL** for database storage.
- **Python** for alerting.
- **Cron** (or equivalent) for task automation.
- **psql** for database queries.

import Credentials
from GenerateMessage import generate_message

FATAL_WALL=Credentials.FATAL
ERROR_WALL=Credentials.ERROR
DB_NAME=Credentials.DB
TABLE_NAME=Credentials.TABLE

def write_alert_file(num_fatals, num_errors):
    temp_string = "-- CURRENT STATUS BELOW --\n"
    temp_string += generate_message(num_fatals,num_errors) # important
    try:
        with open("DUMMY_PATH.txt", 'w') as file: #alert is in the same directory as this script
            file.write(temp_string)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if file: #thanks to the "with" we should be fine, but include this anyway
            file.close()
# we generate the same thing so many times we might as well make it a function
import Credentials
from datetime import datetime
FATAL_WALL=Credentials.FATAL
ERROR_WALL=Credentials.ERROR
DB_NAME=Credentials.DB
TABLE_NAME=Credentials.TABLE

def generate_message(num_fatals, num_errors):
    current_time = datetime.now().time()
    temp_string="Time of Message: {0}\n".format(current_time)
    if(num_fatals >= FATAL_WALL):
        temp_string += "!! CRITICAL ALERT !!\n"
        temp_string += "FATAL THRESHOLD ({0}) REACHED ({1}) - THE FOLLOWING SECTIONS SHOULD BE CHECKED ASAP:\n".format(str(FATAL_WALL),num_fatals)
        temp_string += "DATABASE:{0}\n".format(DB_NAME)
        temp_string += "TABLE:{0}\n".format(TABLE_NAME)
        temp_string += "\n"
    if(num_errors >= ERROR_WALL):
        temp_string += "!! ALERT !!\n"
        temp_string += "ERROR THRESHOLD ({0}) REACHED ({1}) - THE FOLLOWING SECTIONS SHOULD BE CHECKED ASAP:\n".format(str(ERROR_WALL),num_errors)
        temp_string += "DATABASE:{0}\n".format(DB_NAME)
        temp_string += "TABLE:{0}\n".format(TABLE_NAME)
        temp_string += "\n"
    if(num_fatals < FATAL_WALL and num_errors < ERROR_WALL):
        temp_string += "No anomalies detected. Current status below."
        temp_string += "DATABASE:{0}\n".format(DB_NAME)
        temp_string += "TABLE:{0}\n".format(TABLE_NAME)
        temp_string += "FATAL COUNT:{0}\n".format(num_fatals)
        temp_string += "ERROR COUNT:{0}\n".format(num_errors)
        temp_string += "\n"
    return temp_string
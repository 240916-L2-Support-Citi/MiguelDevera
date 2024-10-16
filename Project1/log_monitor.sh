#!/bin/bash

# setting up
DB_NAME="p1test"
DB_USER="miguel"
DB_TABLE="log_entries.log_issues"
#clean up stuff
ARCHIVE="./archive.log"
LOGFILE="./app.log"

while IFS= read -r line; do
    message="$line"

    part1=$(echo "$message" | awk '{print $1, $2}')
    part2=$(echo "$message" | awk '{print $3}')
    part3=$(echo "$message" | awk '{for (i=4; i<=NF; i++) printf $i" "; print ""}' | sed "s/'/''/g")

    # Output the parts
    if [[ "$part2" == "[FATAL]" || $part2 == "[ERROR]" ]];
    then
        psql -U "$DB_USER" -d "$DB_NAME" -c "PREPARE log_insert (timestamp, text, text) AS INSERT INTO $DB_TABLE (timestamp, errorlevel, message) VALUES (\$1, \$2, \$3); EXECUTE log_insert('$part1', '$part2', '$part3');"
    fi
done < "$LOGFILE"

# append the log contents to the archive file
cat "$LOGFILE" >> "$ARCHIVE"

# clear the log file by shoving *nothing* into it
> "$LOGFILE"
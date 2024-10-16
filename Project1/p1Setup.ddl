CREATE SCHEMA log_entries;

DROP TABLE IF EXISTS log_entries.log_issues;

CREATE TABLE log_entries.log_issues(
    id SERIAL PRIMARY KEY, 
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    errorlevel VARCHAR(10) CHECK (errorlevel IN ('[ERROR]', '[FATAL]','[INFO]', '[WARNING]')),
    message VARCHAR(255) DEFAULT 'EMPTY MESSAGE'
    );

ALTER TABLE log_entries.log_issues
ADD CONSTRAINT unique_log
UNIQUE (timestamp, errorlevel, message);
 -- we made only one table because it seems like multiple tables are unneeded - an alert seems like one object
 -- the error level shouldnt count info or warning, but have it here for posterity
 -- timestamp defaults to current time just so we have an estimate of when it happened
 -- all the messages we have in generate_logs.sh have content but we set a default just in case
 -- alternatively we could make it so it can't be empty
 -- that alter just exists to ensure we have no duplicate data
 -- use psql -U username -d database_name -f /path/to/your/file
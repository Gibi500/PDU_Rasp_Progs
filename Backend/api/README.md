# Backend

What I want to make is a backend that is the entry point and exit point for the data. The backend will be a REST API that will be used to get the data from the database and send the data to the database. The backend will also be used to send the data to the frontend and to the screen. The backend wil be written in JS. fot the Database I will use postgreSQL.

## database

The concept is simple there are tables for every type of measurement. So the every table stores the data and the time between the measurements. and most importantly the id of the device is stored in the table.

### Installation of postgreSQL


### Create a database

to create the table use the init.sql file in the initdb folder. 

```bash
psql -U postgres -f initdb/init.sql
```

## API



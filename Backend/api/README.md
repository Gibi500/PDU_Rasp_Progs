# Backend

What I want to make is a backend that is the entry point and exit point for the data. The backend will be a REST API that will be used to get the data from the database and send the data to the database. The backend will also be used to send the data to the frontend and to the screen. The backend wil be written in JS. fot the Database I will use postgreSQL.

## database

The concept is simple there are tables for every type of measurement. So the every table stores the data and the time between the measurements. and most importantly the id of the device is stored in the table.

### Installation of postgreSQL

```bash
apt install postgresql postgresql-client-16
```

### Create a database

to create the table use the init.sql file in the initdb folder.
Please change the path to the file to the correct path and use the absolute path for the least trouble.

```bash
psql -d power_switch_devices -U postgres -f /home/Power/PDU_Rasp_Progs/Backend/initdb/init.sql
```

## API

### installation of nodejs

```bash
apt install nodejs npm
```

### installation of the required packages

go in the api folder and run the following command:
```bash
npm install
```
It uses the package.json file to install al the required packages.

### vulnerabilities

if the npm audit gives vulnerabilities you can run the following command to fix the vulnerabilities:

```bash
npm audit fix
```

### run the server

Before you can run the server you have to make a .env file you can copy the .env.example file and change the values to your own values.
easy command to copy the file:

```bash
cp .env_example .env
```

to run the server you can run the following command:

```bash
npm start
```
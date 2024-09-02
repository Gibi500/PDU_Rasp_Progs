require('dotenv').config({ path: __dirname + '/.env' })
const pool = require('./config/database');

const express = require('express')
const app = express()
const port = process.env['PORT']
const measurementsRouter = require('./routes/measureRoutes');

app.use(express.json());

app.use('/measurements', measurementsRouter);

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

// const mysql = require('mysql2');


// connection.connect((err) => {
//     if (err) {
//         console.log('Error connecting to database:', err);
//         return;
//     }
//     console.log("Connected to database pizza");
// });


// app.post('/', (req, res) => {

//     connection.query('INSERT INTO types SET ?', newRecord, (err, result) => {
//         if(err) {
//             console.error("Error executing query:", err);
//             res.status(500).send('Error executing query');
//             return;
//         }
//         console.log('Record inserted succesfully:', result);
//         res.status(201).json(result);
//     })
// });
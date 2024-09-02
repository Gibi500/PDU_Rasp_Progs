var pool = require('../config/database');

var QueryForLatestMeasurement = `SELECT voltage_measurements.dev_id, voltage_measurements.voltage, current_measurements.current, active_power_measurements.power AS active_power, imaginary_power_measurements.power AS imaginary_power, apparent_power_measurements.power AS apparent_power, power_factor_measurements.power_factor, peak_current_measurements.peak_current
                                FROM voltage_measurements
                                FULL JOIN current_measurements ON voltage_measurements.dev_id = current_measurements.dev_id
                                FULL JOIN active_power_measurements ON voltage_measurements.dev_id = active_power_measurements.dev_id
                                FULL JOIN imaginary_power_measurements ON voltage_measurements.dev_id = imaginary_power_measurements.dev_id
                                FULL JOIN apparent_power_measurements ON voltage_measurements.dev_id = apparent_power_measurements.dev_id
                                FULL JOIN power_factor_measurements ON voltage_measurements.dev_id = power_factor_measurements.dev_id
                                FULL JOIN peak_current_measurements ON voltage_measurements.dev_id = peak_current_measurements.dev_id
                                WHERE voltage_measurements.dev_id = $1 ORDER BY voltage_measurements.created DESC LIMIT 1;`

const data_commands = Object.freeze({
	VOLTAGE: 0,
	CURRENT: 1,
	POWER_ACTIVE: 2,
	POWER_IMAGINARY: 3,
	POWER_APPARENT: 4,
	POWER_FACTOR: 5,
	PEAK_CURRENT: 6
});

exports.postMeasurement = function(req, res, next) {
    console.log(req.body);

    // Extract data from request body intro variables
    let { device_id, type_data, value_data, delta_time} = req.body;

    // Check if variables are int, float and float
    let dataValid = (
        Number.isInteger(device_id) &&
        typeof type_data == 'number' &&
        typeof value_data == 'number' &&
        typeof delta_time == 'number'
    )

    if (dataValid) {
        // DO NOT insert user generated values into the string directly
        let insertSQL
        switch (type_data) {
            case data_commands.VOLTAGE:
                insertSQL = `INSERT INTO voltage_measurements(dev_id, voltage, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.CURRENT:
                insertSQL = `INSERT INTO current_measurements(dev_id, current, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.POWER_ACTIVE:
                insertSQL = `INSERT INTO active_power_measurements(dev_id, power, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.POWER_IMAGINARY:
                insertSQL = `INSERT INTO imaginary_power_measurements(dev_id, power, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.POWER_APPARENT:
                insertSQL = `INSERT INTO apparent_power_measurements(dev_id, power, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.POWER_FACTOR:
                insertSQL = `INSERT INTO power_factor_measurements(dev_id, power_factor, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            case data_commands.PEAK_CURRENT:
                insertSQL = `INSERT INTO peak_current_measurements(dev_id, peak_current, delta_time_from_last_measurement) VALUES ($1, $2, $3);`
                break;
            default:
                res.status(400).send('Invalid data type\n');
                break;
        }

        let values = [(device_id + 1), value_data, delta_time]
        // Pass an array of values as the second 
        // argument for pool.query() method to 
        // build the query string safely.
        pool.query(insertSQL, values, (error, result) => {
            if (error) {
                console.log(error);
                res.status(400).send(error);
            } else {
                res.status(200).send('Saved to database.\n');
            }
        });

    } else {
        res.status(400).send('Please check that your data types are correct');
    }

}

exports.getLatestMeasurementDevice1 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [1], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice2 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [2], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice3 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [3], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice4 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [4], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice5 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [5], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice6 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [6], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice7 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [7], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}

exports.getLatestMeasurementDevice8 = function(req, res, next) {
    // Get most recent measurement from db and return as JSON.
    pool.query(QueryForLatestMeasurement, [8], (error, results) => {
        if (error){
            res.status(400).send(error);
        } else {
            res.status(200).json(results.rows);
        }        
    });
}
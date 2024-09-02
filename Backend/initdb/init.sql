DROP TABLE devices CASCADE;

CREATE TABLE IF NOT EXISTS devices(
    dev_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO devices (name) VALUES 
('Device 1'),
('Device 2'),
('Device 3'),
('Device 4'),
('Device 5'),
('Device 6'),
('Device 7'),
('Device 8');



CREATE TABLE IF NOT EXISTS voltage_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  voltage FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS current_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  current FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS active_power_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  power FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS imaginary_power_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  power FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS apparent_power_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  power FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS power_factor_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  power_factor FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);

CREATE TABLE IF NOT EXISTS peak_current_measurements(
  id SERIAL NOT NULL PRIMARY KEY,
  dev_id INT,
  peak_current FLOAT,
  delta_time_from_last_measurement FLOAT,
  created TIMESTAMP DEFAULT NOW(),
    CONSTRAINT devices
        FOREIGN KEY(dev_id)
            REFERENCES devices(dev_id)
);
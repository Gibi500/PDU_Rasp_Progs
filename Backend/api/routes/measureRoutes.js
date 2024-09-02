var express = require('express');
var router = express.Router();
var measurements = require('../controllers/measureControllers');

router.post('/', measurements.postMeasurement);

router.get('/latest/device1', measurements.getLatestMeasurementDevice1);
router.get('/latest/device2', measurements.getLatestMeasurementDevice2);
router.get('/latest/device3', measurements.getLatestMeasurementDevice3);
router.get('/latest/device4', measurements.getLatestMeasurementDevice4);
router.get('/latest/device5', measurements.getLatestMeasurementDevice5);
router.get('/latest/device6', measurements.getLatestMeasurementDevice6);
router.get('/latest/device7', measurements.getLatestMeasurementDevice7);
router.get('/latest/device8', measurements.getLatestMeasurementDevice8);

module.exports = router;
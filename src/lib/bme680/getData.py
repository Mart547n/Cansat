import bme680, time 

# Creates an instance of the sensor
sensor = bme680.BME680()

# Costumises the settings for the sensor (takes care of how long each mesurement lasts)
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_4x)

# Filters the values (makes the readings more stable)
sensor.set_filter(bme680.FILTER_SIZE_3)

""" 
# Used for capturing gas data:
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
"""

while True:
   if sensor.get_sensor_data():
         output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)

         print(output)

   time.sleep(1)
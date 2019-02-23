import bme680, time

class Bme680:

   def __init__ (self, addFilter = False):
      # Initialisation:
      try:
         self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
      except IOError:
         self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
      self.applySensorSettings()

      if (addFilter == True):
         # Adds a filter on top of the readings (Makes the more stable)
         self.sensor.set_filter(bme680.FILTER_SIZE_3)

   def applySensorSettings (self):
      # Applies the settings to the sensor 
      self.sensor.set_humidity_oversample(2)
      self.sensor.set_pressure_oversample(2)
      self.sensor.set_temperature_oversample(2)

   def readTemperature(self):
      # Reads and return temperture data:
      try:
         if (self.sensor.get_sensor_data() == True):
            return self.sensor.data.temperature
         else: 
            return None
      except IOError:
         return None
   
   def readPresure(self):
      # Reads and returns Presure data:
      if (self.sensor.get_sensor_data() == True):
         return self.sensor.data.temperature
      else: 
         return None

   def readHumidity(self):
      # Reads and returns Humidity data:
      if (self.sensor.get_sensor_data() == True):
         return self.sensor.data.temperature
      else: 
         return None

   def ready(self):
      # Returns a bool (wether or not the sensor is ready or not)
      return self.sensor.get_sensor_data()

if (__name__ == "__main__"):
   sensor = Bme680(addFilter = True)
   while (True):
      if (sensor.ready() == True):
         print("{0} Degrees".format(sensor.readTemperature))

      time.sleep(1)
      
import bme680, time
from helper import logMsg

class Bme680:
   def __init__ (self, addFilter = False):
      # Initialisation:
      try:
         self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
         logMsg("bme680 setup at primary adress")
      except IOError:
         self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
         logMsg("bme680 setup at secondary adress")
      self.applySensorSettings()

      if (addFilter == True):
         # Adds a filter on top of the readings (Makes the more stable)
         self.sensor.set_filter(bme680.FILTER_SIZE_3)
         logMsg("Filter turned On")
      else: 
         logMsg("Filter Turned Of")

   def timeReadings(self):
      # Returns the time in ms it takes to get the outputs
      startTime = time.time()
      temperature = self.readTemperature()
      presure = self.readPresure()
      humidity = self.readHumidity()
      return (time.time() - startTime)

   def applySensorSettings (self):
      # Applies the settings to the sensor 
      self.sensor.set_humidity_oversample(2)
      self.sensor.set_pressure_oversample(2)
      self.sensor.set_temperature_oversample(2)

   def readTemperature(self):
      # Reads and return temperture data:
      try:
         return "{0:10.f}".fomrat(self.sensor.data.temperature)
      except IOError:
         return None
   
   def readPresure(self):
      # Reads and returns Presure data:
      try:
         return "{0:10.4f}".format(self.sensor.data.pressure)
      except IOError:
         return None

   def readHumidity(self):
      # Reads and returns Humidity data:
      try:
         return "{0:10.4f}".format(self.sensor.data.humidity)
      except IOError:
         return None

   def ready(self):
      # Returns a bool (wether or not the sensor is ready or not)
      return self.sensor.get_sensor_data()

if (__name__ == "__main__"):
   startTime = time.time()
   sensor = Bme680(addFilter = True)
   timeToTakeReadings = sensor.timeReadings()
   print("Time to take readings {0} ms".format(timeToTakeReadings))
   while (True):
      if (sensor.ready() == True):
         print("time: {0} s , {1} Degrees \n {2} hPa \n {3} % RH".format((time.time() - startTime), 
                                                                          sensor.readTemperature(),
                                                                          sensor.readPresure(), 
                                                                          sensor.readHumidity()))
         
      time.sleep(0.5 - (timeToTakeReadings/1000))
      
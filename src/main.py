import time
from bme680DriverCode import *
from logger import Logger

if (__name__ == "__main__"):
    # Initialing interfaces ect.
    print("Botting up...\nInitialising logging interface.")
    logger = Logger()
    time.sleep(0.3)
    print("Logger initialised! \nInitialising sensor interface..")
    sensor = Bme680(addFilter = True)
    timeDelay = sensor.timeReadings()
    time.sleep(0.5)
    print("Sensor Interface initialised.")
    print("Main loop starting...")
    # Main loop
    startTime = time.time()
    while (time.time() - startTime >= 120.0):
        if (sensor.ready() == True):
         logger.saveData("temp", logger.getTimeMiliSec(), data = sensor.readTemperature)
         print("time: {0} s , {1} Degrees \n {2} hPa \n {3} % RH".format((time.time() - startTime), 
                                                                          sensor.readTemperature(),
                                                                          sensor.readPresure(), 
                                                                          sensor.readHumidity()))
         
        time.sleep(0.3)
from data import *
from helper import help 
import time
import bme680

if (__name__ == '__main__'):
   # it's the main program bitches 
   sTime = getTimeMiliSec()
   #bmeSensor = bme680.Bme680()
   while ((getTimeMilisec() - sTime) < (5 * 1000)): # Runs the loop for 5 seconds
      print("fuck of ")
      time.sleep(1)


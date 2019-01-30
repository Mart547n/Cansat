from bmp280 import *
from mpu9250 import *

if (__name__ == '__main__'):
   # Perform test
   bmp = BMP280()
   print("bmp data:  {0}".format(bmp.readAll()))
   mpu = MPU9250()
   print("mpu data: temp: {0}, accel: {1}".fromat(mpu.readTemp, mpu.readAccel))
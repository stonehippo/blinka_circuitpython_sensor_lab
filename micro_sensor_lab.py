import board
from time import sleep
from adafruit_veml7700 import VEML7700
from adafruit_bme680 import Adafruit_BME680_I2C
from adafruit_lis3mdl import LIS3MDL
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3

i2c = board.I2C()
bme = Adafruit_BME680_I2C(i2c)
accel_gyro = LSM6DS3(i2c)
mag = LIS3MDL(i2c)
light = VEML7700(i2c)

def get_bme():
   # BME688 temp, pressure, humidity, and gas sensor
  print(f"Current temp: {round(bme.temperature, 2)} ºC")
  print(f"Current relative humidity: {round(bme.relative_humidity, 2)} %")
  print(f"Current VOC gas: {round(bme.gas, 2)} ohm")
  print(f"Current altitude: {round(bme.altitude, 2)} meters")
  
def get_accel_gyro():
   # LSM6DS3 accelerometer + gyroscope
  accel_x, accel_y, accel_z = accel_gyro.acceleration
  gyro_x, gyro_y, gyro_z = accel_gyro.gyro
  print(f"Accel: X: {accel_x} Y: {accel_y} Z: {accel_z}")
  print(f"Gyro: X: {gyro_x} Y: {gyro_y} Z: {gyro_z}")
  
  # LIS3MDL magnetometer
  mag_x, mag_y, mag_z = mag.magnetic
  print(f"Mag: X: {mag_x} Y: {mag_y} Z: {mag_z}")

def get_light():
  # VEML7700 Light Sensor
  print(f"Light level: {light.lux} lux")

# basic usage is pretty easy: just read the values from the sensors
# take a look at the documentation for each sensor to understand optional configuration
while True:
  get_bme()
  print("\n------------\n")
  get_light()
  print("\n------------\n")
  get_accel_gyro()
  print("\n------------\n")
  sleep(0.5)
import smbus
import time

#To get a mesure, we need to write 0x04 in the register 0x00 then read the register 0x8f and transform its result.

bus = smbus.SMBus(1)             # I2C Bus for a RaspberryPi 2
LIDARLite_ADDRESS = 0x62         # I2C address of the LidarLite device
RegisterMeasure = 0x00           # Register to write to initiate ranging.
MeasureValue = 0x04              # Value to initiate ranging.
RegisterHighLowB = 0x8f          # Register to get both High and Low bytes in 1 call.


def I2C_write(register,value):
        bus.write_byte_data(LIDARLite_ADDRESS, register, value)


def I2C_read(register):
        value = bus.read_byte_data(LIDARLite_ADDRESS, register)
        return(value)


try:
    while True:
        I2C_write(RegisterMeasure,MeasureValue)
        time.sleep(0.5)
        read8f = I2C_read(0x90)
        print read8f

except KeyboardInterrupt:

    print "   !!!!Ctrl C detected !!!!! GoodBye"

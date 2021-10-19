#!/usr/bin/python
import smbus
import math
import time 

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
	return bus.read_byte_data(address, reg)
	
def read_word(reg):
	h = bus.read_byte_data(address, reg)
	l = bus.read_byte_data(address, reg+1)
	value = (h << 8) + l
	return value

def read_word_2c(reg):
	val = read_word(reg)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val
		
def dist(a,b):
	return math.sqrt((a*a)+(b*b))
	
def get_y_rotation(x,y,z):
	radians = math.atan2(x, dist(y,z))
	return -math.degrees(radians)
	
def get_x_rotation(x,y,z):
	radians = math.atan2(y, dist(x,z))
	return math.degrees(radians)
	
bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68 			# via i2detect

bus.write_byte_data(address, power_mgmt_1, 0)

while True:
	
	print "Gyroskop"
	print "--------"

	gyroskop_xout = read_word_2c(0x43)
	gyroskop_yout = read_word_2c(0x45)
	gyroskop_zout = read_word_2c(0x47)

	print "gyroskop_xout: ", ("%6d" % gyroskop_xout), " skaliert: ", (gyroskop_xout / 131)
	print "gyroskop_yout: ", ("%6d" % gyroskop_yout), " skaliert: ", (gyroskop_yout / 131)
	print "gyroskop_zout: ", ("%6d" % gyroskop_zout), " skaliert: ", (gyroskop_zout / 131)

	print "Beschkeunigungssensor"
	print "--------"

	beschkeunigung_xout = read_word_2c(0x3b)
	beschkeunigung_yout = read_word_2c(0x3d)
	beschkeunigung_zout = read_word_2c(0x3f)

	beschkeunigung_xout_skaliert = beschkeunigung_xout / 16384.0
	beschkeunigung_yout_skaliert = beschkeunigung_yout / 16384.0
	beschkeunigung_zout_skaliert = beschkeunigung_zout / 16384.0

	print "beschkeunigung_xout: ", ("%6d" % beschkeunigung_xout), " skaliert: ", beschkeunigung_xout_skaliert
	print "beschkeunigung_yout: ", ("%6d" % beschkeunigung_yout), " skaliert: ", beschkeunigung_yout_skaliert
	print "beschkeunigung_zout: ", ("%6d" % beschkeunigung_zout), " skaliert: ", beschkeunigung_zout_skaliert


	print "X rotation: ", get_x_rotation(beschkeunigung_xout_skaliert,beschkeunigung_yout_skaliert,beschkeunigung_zout_skaliert)
	print "Y rotation: ", get_y_rotation(beschkeunigung_xout_skaliert,beschkeunigung_yout_skaliert,beschkeunigung_zout_skaliert)
	time.sleep(0.2)

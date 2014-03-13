#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

runningtotal = 0.0
transactiontotal = 0.0
pennies = 0
nickels = 0
dimes = 0
quarters = 0

def waitForButton():
	global pennies
	global nickels
	global dimes
	global quarters
	global runningtotal
	global transactiontotal
	while (GPIO.input(17)):
		coinval = port.read(1)
		if (len(coinval) is 0):
			continue
		else:
			coinval = ord(coinval)
		if   coinval == 1:
			print "You got a penny!"
			pennies += 1
			runningtotal += .01
			transactiontotal += .01
		elif coinval ==  5:
			print "You got a nickel!"
			nickels+= 1
			runningtotal += .05
			transactiontotal += .05
		elif coinval == 10:
			print "You got a dime!"
			dimes+= 1
			runningtotal += .10
			transactiontotal += .10
		elif coinval == 25:
			print "That was a quarter!"
			quarters+= 25
			runningtotal += .25
			transactiontotal += .25
	print "button was pushed"

while True:
	print "put some money in"
	waitForButton();
	print transactiontotal
	print pennies
	time.sleep(5) #this is where we print
	transactiontotal = 0.

#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO
import time

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

runningtotal = 0.0
totalpennies = 0
totalnickels = 0
totaldimes = 0
totalquarters = 0

def waitForButton():
	pennies = 0
	nickels = 0
	dimes = 0
	quarters = 0
	transactiontotal = 0.0
	while (GPIO.input(17)):
		coinval = port.read(1)
		if (len(coinval) is 0):
			continue
		else:
			coinval = ord(coinval)
		if   coinval == 1:
			print "You got a penny!"
			pennies += 1
			transactiontotal += .01
		elif coinval ==  5:
			print "You got a nickel!"
			nickels+= 1
			transactiontotal += .05
		elif coinval == 10:
			print "You got a dime!"
			dimes+= 1
			transactiontotal += .10
		elif coinval == 25:
			print "That was a quarter!"
			quarters+= 25
			transactiontotal += .25
	print "button was pushed"
	return (transactiontotal, pennies, nickels, dimes, quarters)

while True:
	print "put some money in"
	transaction = waitForButton();
	print "before runningtotal is", runningtotal, "pennies total", totalpennies
	runningtotal += transaction[0]
	totalpennies += transaction[1]
	print "runningtotal is", runningtotal, "pennies total", totalpennies
	time.sleep(5) #this is where we print
	transactiontotal = 0.

#!/usr/bin/env python
from Adafruit_PWM_Servo_Driver import PWM
import time
import atexit
import curses

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.addstr(0,10,"hit 'q' to quit")
stdscr.refresh()
key=''

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

def sendLook(in1, in2):
    pwm.setPWM(0, 0, in1)
    pwm.setPWM(1, 0, in2)

def setStop():
    A0 = 0
    A1 = 0
    B0 = 0
    B1 = 0

def release():
    sendRun(0, 0, 0, 0)
    sendLook((servoMin + servoMax) / 2,(servoMin + servoMax) / 2)
    curses.endwin()

pwm = PWM(0x40, debug=False)

servoMin = 150
servoMax = 600
step = 1

pwm.setPWMFreq(50)

A0 = 0
A1 = 0
B0 = 0
B1 = 0

C0 = (servoMin + servoMax) / 2
C1 = (servoMin + servoMax) / 2
sendLook(C0, C1)

# Try and run the main code, and in case of failure we can stop the motors
try:
    # This is the main loop
    while True:
	if key == ord('q'):
            break	
	key = stdscr.getch()
        stdscr.refresh()
        look = False
        run = False
        if key >= ord('1') and key <= ord('9'):
            step = key - ord('0')
	if key == curses.KEY_DOWN:
            look = True
            stdscr.addstr(2,20,"DOWN")
            if C0+step <= servoMax:
                C0+=step
        if key == curses.KEY_UP:
            look = True
            stdscr.addstr(2,20,"UP")
            if C0-step >= servoMin:
                C0-=step
        if key == curses.KEY_LEFT:
            look = True
            stdscr.addstr(2,20,"LEFT")
            if C1+step < servoMax:
                C1+=step
        if key == curses.KEY_RIGHT:
            look = True
            stdscr.addstr(2,20,"RIGHT")
            if C1-step >= servoMin:
                C1-=step
        if look:
            sendLook(C0, C1)

except KeyboardInterrupt:
    release()

atexit.register(release)

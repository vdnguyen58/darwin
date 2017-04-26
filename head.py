#!/usr/bin/env python
from Adafruit_PWM_Servo_Driver import PWM
import time
import atexit

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)

class RobotHead():

  pwm = PWM(0x40, debug=False)
  servoMin = 150
  servoMax = 600
  step = 1  
  C0 = (servoMin + servoMax) / 2
  C1 = (servoMin + servoMax) / 2
  
  def __init__(self):
    self.pwm.setPWMFreq(50)
    self.sendLook(self.C0, self.C1)

  def setServoPulse(self, channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

  def sendLook(self, in1, in2):
    self.pwm.setPWM(0, 0, in1)
    self.pwm.setPWM(1, 0, in2)

  def release(self):
    self.sendLook((self.servoMin + self.servoMax) / 2,(self.servoMin + self.servoMax) / 2)
    
  def lookUp(self):	
    if self.C0-self.step >= self.servoMin:
      self.C0-=self.step
    self.sendLook(self.C0, self.C1)

  def lookDown(self):
    if self.C0+self.step <= self.servoMax:
      self.C0+=self.step
    self.sendLook(self.C0, self.C1)	

  def lookLeft(self):
    if self.C1+self.step < self.servoMax:
      self.C1+=self.step
    self.sendLook(self.C0, self.C1)   

  def lookRight(self):
    if self.C1-self.step >= self.servoMin:
      self.C1-=self.step
    self.sendLook(self.C0, self.C1)

  def test(self):
    for x in range(self.servoMin, self.servoMax):
      self.lookLeft()
    for x in range(self.servoMin, self.servoMax):
      self.lookRight()
    for x in range(self.servoMin, self.servoMax):
      self.lookUp()
    for x in range(self.servoMin, self.servoMax):
      self.lookDown()
    self.release()
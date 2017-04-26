#!/usr/bin/python

import time
from Adafruit_PWM_Servo_Driver import PWM

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)

class RobotBase():
  pwm = PWM(0x40, debug=True)

  servoMin = 175
  servoMax = 625

  def setServoPulse(self, channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    self.pwm.setPWM(channel, 0, pulse)

  def sendPWM(self, mtNum, en, in1, in2):
    en *= 4095
    in1 *= 4095
    in2 *= 4095
    self.pwm.setPWMFreq(50)
    if (mtNum == 0):
        self.pwm.setPWM(2, 0, en)
        self.pwm.setPWM(4, 0, in1)
        self.pwm.setPWM(5, 0, in2)
    else:
        self.pwm.setPWM(3, 0, en)
        self.pwm.setPWM(6, 0, in1)
        self.pwm.setPWM(7, 0, in2)

  def stop(self):
    print "turn on"
    # left wheel
    self.sendPWM(0, 1, 0, 0)
    # right wheel
    self.sendPWM(1, 1, 0, 0)
    # i.e.: turn left(0) wheel on(1) and set the state to stop(0), (0)

  def turnoff(self):
    print "turn off"
    self.sendPWM(0, 0, 0, 0)
    self.sendPWM(1, 0, 0, 0)

  def forward(self):
    print "forward"
    self.sendPWM(0, 1, 0, 1)
    self.sendPWM(1, 1, 1 ,0)
    # turn left wheel (0) on (1) and let it run forward (0, 1)
    # turn right wheel (1) on (1) and let it run backward (1, 0)

  def backward(self):
    print "backward"
    self.sendPWM(0, 1, 1, 0)
    self.sendPWM(1, 1, 0, 1)

  def test(self):
    self.forward()
    time.sleep(10)
    self.stop()
    time.sleep(10)
    self.backward()
    time.sleep(10)
    self.stop()

darwin=RobotBase()
darwin.test()

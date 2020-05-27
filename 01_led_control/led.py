from machine import Pin, PWM

class LED(object):
	def __init__(self):
		self.pwm0 = PWM(Pin(0), freq=1000, duty=512) 
		self.pwm4 = PWM(Pin(4), freq=1000, duty=512) 
		self.pwm5 = PWM(Pin(5), freq=1000, duty=512) 

	def set(self, dic):
		self.pwm0.duty(dic['r'])
		self.pwm4.duty(dic['g'])
		self.pwm5.duty(dic['b'])


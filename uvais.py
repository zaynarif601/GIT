import serial,time 
from matplotlib import pyplot

#device name. BAUD Rate ( Speed ), timeout=1 second
s = serial.Serial('COM4',38400,timeout=2)
s.readline()

time.sleep(1) 

#QUERY INSTRUMENT ID
s.write(b'*IDN?\n')

print(s.readline())

def query(cmd):
	s.write((cmd+'\n').encode())
	return s.readline().strip().decode()
	
def write(cmd):
	s.write((cmd+'\n').encode())

print(query('*IDN?'))
print(query('MEAS:0?'))

pyplot.ion()
pyplot.show()

for a in range(100):
	pyplot.scatter( a, float((query('MEAS:0?')) ) )
	write('RED:ON')
	pyplot.pause(0.1)
	write('RED:OFF')
	pyplot.pause(0.1)

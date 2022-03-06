#!/usr/bin/python3
""" 
This program tries to present a simple example for creating a stable actuator
output from a single, possibly unstable sensor. Samples from the 'history' or 
register are then averaged into a result.

The higher the ‘_samples’ count the more stabilized the output but depending 
on the system in place maybe to stabilized. 
The lower the ‘_samples’ count the more unregulated the output
"""

from statistics import mean

_samples = 10
_register = [_samples]
_debug = True

def takeSample():
	""" This method asks to take a sample """

	print("Please enter number:")
	sample = input()

	_register.append(int(sample))

	return True

def processSample():
	""" This method processes samples to a buffer and returns a average """

	if len(_register) > _samples:
		_register.pop(0)

		if debug: print(_register)

		return mean(_register)

	else: return None
	
def main():
	""" This is the projects control method """

	# this is to just keep asking the user
	while True:

		# read sensor input
		takeSample()
		# process the inputs into a collection of samples
		result = processSample()

		# check if the the registers 'history' has a desired state
		if result != None:
			print("The average of the value taken is:", result)
			# use this result as regulated output for actuators
		else:
			print("There are not enough values to process")

main()
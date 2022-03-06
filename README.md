# shift_register
This program tries to present a simple example for creating a stable actuator
output from a single, possibly unstable sensor. Samples from the 'history' or 
register are then averaged into a result.

The higher the 'samples' count the more stabilized the output but depending 
on the system in place maybe too stabilized. 
The lower the 'samples' count the more unregulated the output

The Arduino microcontroller is a small, inexpensive computer that makes it easy for any 
computer to interact with the outside world.  It accepts input from sensors, sends output to motors,
solenoids, lights etc.   I write a little program in C++ and put it in the little computer (Arduino Uno)
and the program accepts input, creates output, and sends out data.  I have little understanding of it,
but it is not difficult to do cool things with it.

The signals come in through a Hall detector.  There is a magnet on the pendulum. 
At the end of its swing the magnet trips the Hall and the signal is sent to the Arduino 
which then sends it out and into a computer through the computer’s serial port.  
In the computer the signal is caught by Python.  This program adds a UNIX time stamp and 
puts it in a  sqlite3 database.

There was an enormous amount of development behind both the C++ and the Python, 
but in the end neither is tremendously complex.

The data streams are through essentially clocks which are both accurate and precise.  
The Python simply separates them by size with ‘if’ statements.    Some of the fields threatened
to overlap with others and I added 30 million and 20 million to two of the data streams respectively.
These were added unambiguously at the input.  With these the Python was able to absolutely separate them. 
And before insertion into the database, the respective 20 and 30 million was subtracted back out.
This repository shows this software.  The languages are C++ and Python and the database is sqlite3. 

Arduino and C++
The rotating pendulums trips the Hall detector twice for every cycle.  This required an extra set of loops within the logic.
The swinging pendulum just catches the Hall at the end of the swing.

Python   libraries:  serial,  sqlite3   datetime.  One connection object.  
It is written with a separate insert for each of the six datastreams.
This is all about SQL.

Supporting documentation       https://app.box.com/s/7bblatfb3j1ioil80ciljrb02d4jq4v6

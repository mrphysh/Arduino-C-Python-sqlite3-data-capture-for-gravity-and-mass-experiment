import serial #import serial library
import sqlite3
import datetime

data_object=serial.Serial("COM3",baudrate=9600 , timeout=3.0)  #  data_object is the object!!
###################
conn = sqlite3.connect ('june26_all_numbers')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS first_table (column_one TEXT,column_two REAL,column_three REAL,\
                column_four REAL, column_five REAL,column_six REAL,column_seven REAL,column_eight REAL )")
#####    
def dynamic_data_entry_column_two():
    
    c.execute("INSERT INTO first_table(column_one,column_two) VALUES (?,?)",
		 ( unix , value_two  ) )
    conn.commit()
def dynamic_data_entry_column_three():
    
    c.execute("INSERT INTO first_table(column_one,column_three) VALUES (?,?)",
		 ( unix , value_three  ) )
    conn.commit()
def dynamic_data_entry_column_four():
    
    c.execute("INSERT INTO first_table(column_one,column_four) VALUES (?,?)",
		 ( unix , value_four  ) )
    conn.commit()
def dynamic_data_entry_column_five():
    
    c.execute("INSERT INTO first_table(column_one,column_five) VALUES (?,?)",#
		 ( unix , value_five  ) )
    conn.commit()
def dynamic_data_entry_column_six():
    
    c.execute("INSERT INTO first_table(column_one,column_six) VALUES (?,?)",
		 ( unix , value_six  ) )
    conn.commit()
def dynamic_data_entry_column_seven():
    
    c.execute("INSERT INTO first_table(column_one,column_seven) VALUES (?,?)",
		 ( unix , value_seven  ) )
def dynamic_data_entry_column_eight():
    
    c.execute("INSERT INTO first_table(column_one,column_eight) VALUES (?,?)",
		 ( unix , value_eight  ) )

    conn.commit()
    ###
create_table()
    
    ##########################
unix = (datetime.datetime.now())
value_two = 0
value_three = 0
value_four = 0
value_five = 0
value_six = 1000
dynamic_data_entry_column_six()
i=0
create_table()
#################
while (1==1):
    value_two = 0;    value_three = 0
    value_four = 0
    value_five = 0
    value_six = 0
    value_five = 0
    value_six = 0
#####

    
    
    
    (data_object.inWaiting()>0)                       ##  this is the input from Arduino
    unix = (datetime.datetime.now())                  ##    make the unicode into string then into int
    
    in_data = data_object.readline().decode('ascii')   ##
    in_data = in_data.encode('utf-8')
    ##in_data=int(in_data)
    print (in_data)
    print (type(in_data))

    ##  this goes out to the python monitor;  every number
    i = i+1
    if (i==19
        ):
        in_data = int(in_data)           ###########  this seems to only work when placed here???

    
    ####    rotating pendulum 2 column and input   rodney  period about 15.1 million millionths
       
        if (in_data > 15220000.0) and (in_data <16000000):
            value_two = in_data
        
            dynamic_data_entry_column_two()
        
  ####   mu    about 1876     3 column and input
        
        elif (in_data > 1850000) and (in_data < 1900000):
            value_three = in_data
            dynamic_data_entry_column_three()
            
 ####   alpha    about 1819     4 column and input     10 million
        
        elif (in_data > 21500000) and (in_data < 22300000):
            value_four = in_data - 20000000
            dynamic_data_entry_column_four()
            
 ###    beta    about 1815     5 column and input      20 million
        
        elif (in_data > 15000000) and (in_data < 15220000):
            value_five = in_data 
            dynamic_data_entry_column_five()
            
 ####   theta    about 1805     6 column and input   30 million
        
        elif (in_data > 31000000.0) and (in_data < 33000000.0):
            value_six = in_data -30000000
            dynamic_data_entry_column_six()
            
 ####   rodney    period about 13.4 milllion     7 column and input   period about 13.1 milllion
        
        elif (in_data > 13000000.0) and (in_data < 14000000.0):
            value_seven = in_data
            dynamic_data_entry_column_seven()
            
####   error       xxxx   error  8 column and input
        
        else:
            value_eight = 69696969
            dynamic_data_entry_column_eight() ##this is the error field
        


    
       
      
         
    else :
        continue
    i=0         

"""   
   This should be collectig one of 19   regular
 




"""

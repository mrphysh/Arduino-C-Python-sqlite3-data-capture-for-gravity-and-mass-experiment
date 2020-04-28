import sqlite3   
import datetime
from datetime import datetime,timedelta #  this looks to be essential
"""
We are taking the datetime out of sqlite3.  But the Python takes the data field
and consdiers it a string regardless of the storage conditions.
In other words, a DATE in sqlite3 is just a string to Python.

Could the whole be ;  just change the input string to a datetime and proceed
from that.  Maybe, but this works for me.

"""


my_string = '2019-10-28 12;00:00'

print (my_string)

print ("the string if of type   ",type(my_string))

my_date = datetime.strptime(my_string, "%Y-%m-%d %H;%M:%S") # this must match the input format.

print (my_date)

print ("new type of my_date",type(my_date))
new_date = my_date + timedelta(hours = 1)    #   this is 'add an hour'  usually 'add one day'
print ("one hour added    ",new_date)

print ()
new_date = new_date + timedelta(hours = 1)
print ("another hour added      ",new_date)

#print ("new type of my_date",type(my_date))
new_date = new_date + timedelta(days = 1)
print ("with a day added  ",new_date)

#datetime.strftime(new_date, "Y%-%m-%d %H:%M:%S")    not necessary
                                              #  does not work
my_strg_two = str(new_date)#  the conversion back to str is just this simple


print ("type after conversion to string",type(my_strg_two))
print (type(my_strg_two), "  is the type for my_strg_two"  )
print ("and the value of my_str_two is ", (my_strg_two))
print ("........okay...........")

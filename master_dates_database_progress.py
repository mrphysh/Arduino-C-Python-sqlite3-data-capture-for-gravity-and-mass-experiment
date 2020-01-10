import sqlite3   
import datetime
from datetime import datetime,timedelta
"""

"""

conn = sqlite3.connect('test_database.db.db')      # one table only 'first_table'
c = conn.cursor()

date_var = '2019-04-07'

print ("++++++++++++++++++")
print (type(date_var)) # ti stays as a <str>
print (date_var)
test_var = datetime.strptime(date_var, "%Y-%m-%d")#  yes this hanges it to a datetime.datetime
print (type(test_var))
print (test_var)
search_number = 2

print()
var_one = 34
print()
number = 0

while ( var_one ):
    print ("for row loop starts here")
    c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %date_var)#
    number =0
    for row in c.fetchmany(search_number):   #use this format for a number of rows.
        
        var_one = row[0]  #row[0 is the datetime]
        print (var_one)
        print()
        print (type(var_one))  #It is a string ,, so the datbase returns a string
        
        print (len(var_one))   #the string business is working
        print (var_one[0:10])
        print (var_one[10:26])
        print (row[0])
        print (row[1])
        print (row[2])
        print (row[3])
       
        number = number +1
    print ("the fetchmany number must have been   ",number)
    
    number = 0
    print ("the date_var is type ", type(test_var))  # is type datetime.datetime&&*^%$#  it is flopping back and forth
                                                     #between <datetime.datetime> and <str>
    print ("*******************************************************")
    
    date = datetime.strptime(date_var, "%Y-%m-%d")  # this sets up the variable for altering
    new_date = date + timedelta(days = 1)     # new_date is created here to accept the next day?
    datetime.strftime(new_date, "%Y-%m-%d")
    date_var = str(new_date)
    print ("          date_var before modification ",  date_var)
    date_var = date_var[0:10]
    print ("           date_var after modifucation", date_var)
    print ("var_one, the datetime trigger is     ",var_one)


   

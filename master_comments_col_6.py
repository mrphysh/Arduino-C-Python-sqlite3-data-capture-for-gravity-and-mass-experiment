import sqlite3    #  just this library
"""
Column_5 and Column_six are extra.  Some table have comments in column_six
The Python 'start' puts a 1000 in column_six
this particular database has almost nothing in these two columns.  This makes a new database

"""

conn = sqlite3.connect('test_database')      # one table only 'first_table'

c = conn.cursor()

c_2 = sqlite3.connect('test_database')

c_2 = conn.cursor()

c_2.execute("CREATE TABLE IF NOT EXISTS new_table (column_one TEXT,  column_five TEXT, six BLOB, column_extra REAL)")
"""
i THINK i NEED A DIFFERENT OBJECT FOR A DIFFERENT TABLE?
no no no   This code works but the same cursor will work for two tables within the same database.  
That makes sense anyway.
"""

def dynamic_data_entry_column_five():
    
    c_2.execute("INSERT INTO new_table(column_one,column_five) VALUES (?,?)", ( var_one , var_five  ) )
    conn.commit()

def dynamic_data_entry_column_six():
    
    c_2.execute("INSERT INTO new_table (column_one , six) VALUES (?,?)", ( var_one, var_six  ) )
    conn.commit()


c.execute ("SELECT column_one, column_five, column_six FROM first_table ")#    

number = 0  # initialize counter for fetch loop
col_five = 0
col_six = 0
for row in c.fetchall():
    var_one     = (row[0])
  
    var_five =  (row[ 1])
    var_six  = (row[2])

    number = number +1
##    if (row[1]):
##        print (row[0])     #  this is col 5
##        print (row[1])
##       
##        col_five = col_five +1
##        dynamic_data_entry_column_five()


        
    if (row[2]):
        print (row[0])     #this is col 6
        print ("                               " , row[2])
        print ("column six comment")  
      
        col_six = col_six +1
        dynamic_data_entry_column_six()


        

    
   
print (number)
print (col_five)
print (col_six)

#  this is almost working





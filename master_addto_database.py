import sqlite3   
import datetime
from datetime import datetime,timedelta
"""
good..  This only lacking the datbase input.
tricks:
the date trip to the next day....described elsewhere
The empty fields are null  Use [if row[2]  null is skip this.
I set this up with colu_one etc.  I do not really know which column is which pendulum
for each pendulum  (for each column)
initialize the two counters, total sum and count number
calculate average after each fetchmany is complete.

......the end of the database is a problem.  When the fetch runs out of rows it needs a stop signal.
The WHILE (if var)  works.  The variale can be given a None.  This is like a nonetype or null
and with this, the WHILE can find a stop signal when the dtabaser runs out of rows.



"""

conn = sqlite3.connect('test_database.db.db')      # one table only 'first_table'
c = conn.cursor()

date_var = '2019-03-02'#  this is an input from the operator.
                    #  The datetime field is really an object(??)
##                    #  but the database only takes it and returns it as a string
##                    So, the string must be turned into an object, incremented
##                    turned back into a string and then chopped down to the correct size with string
##                    manupulation
                   # But it works fine.
                   
c.execute("CREATE TABLE IF NOT EXISTS summary_table_practice (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )") 
print ("++++++++++++++++++")
print (type(date_var)) # ti stays as a <str>
print (date_var)
def dynamic_data_entry_averages():
    
    c.execute("INSERT INTO summary_table_practice(column_one,column_two,column_three,column_four) VALUES (?,?,?,?)",
		 ( date_var, col_two_avg  , col_thr_avg  ,  col_for_avg  ) )
    conn.commit()




search_number = 800

#
print()
var_one = 34 # need something here
print()
number = 0
total_count = 0
while (var_one  ):
    var_one = None  ####   yes  yes  yes.  This worked.  make it null and if this is not
                            ## reinitialized the while  statement is stoppped
  #  print ("    $$$$$$$$$$     for row loop starts here          $$$$$$$$$$$$$")
    c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %date_var)#
    number =0                      #  this is the count for that fetch
                                   #  it is reinitialized, but also  used for a total count
    
    col_two_sum   = 0              #   these need to be reinitialized
    col_two_count = 0
    
    col_thr_sum   = 0
    col_thr_count = 0
    col_for_sum   = 0
    col_for_count = 0
    
    for row in c.fetchmany(search_number):   #use this format for a number of rows.
                                            # In the final rendition, this might be 6000
                                              #  there are about 7000 records per day.
        
        var_one = row[0]  #row[0 is the datetime]  and this is the trigger for the WHILE
##        print ("                        datetime row [0] is               ",(row[0]))
##        print ("                        column_two row[1] is              ",  (row[1]))
##        print ("                        column_three          row 2 is    "    ,(row[2]))
##        print ("                        columnumn_four row[3] is          ",  (row[3]))
##
       
        if (row[1])!= None:
            col_two_sum = col_two_sum + (row[1])
            col_two_count= col_two_count +1
      #      print("col_two_count and col_two      ", col_two_count,"     alpha_sum   ", col_two_sum)
        if (row[2])!= None:
            col_thr_sum = col_thr_sum + (row[2])
            col_thr_count= col_thr_count +1
        #    print("col_thr_count and col_thr_sum      ", col_thr_count,"     alpha_sum   ", col_thr_sum)
        if (row[3])!= None:
            col_for_sum = col_for_sum + (row[3])
            col_for_count= col_for_count +1
        #    print("col_four_count and col_four_sum      ", col_for_count,"     alpha_sum   ", col_for_sum)

        number = number +1
        
    
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
##    print ("*******************************************************")
    
    date = datetime.strptime(date_var, "%Y-%m-%d")  # this sets up the variable for altering
    new_date = date + timedelta(days = 1)     # new_date is created here to accept the next day?
    #datetime.strftime(new_date, "%Y-%m-%d")  # the object is turned back into a string  no??
    date_var = str(new_date)
    if (col_two_sum > 1500000):
        
        col_two_avg = col_two_sum/(col_two_count )
       # print ("          the average for col_two for this day is ",  col_two_avg)
    if (col_thr_sum > 1500000):
        ######  this is not  calculating correctly
        col_thr_avg = col_thr_sum/(col_thr_count )
       # print ("          the average for col_thr for this day is ",  col_thr_avg)
    if (col_for_sum > 1500000):
        
        col_for_avg = col_for_sum/(col_for_count )
       # print ("          the average for col_for for this day is ",  col_for_avg)


    dynamic_data_entry_averages()    
    date_var = date_var[0:10]  #  the var_date trigger for the while statement needs the same size and format
   # print ("           date_var after modification", date_var)
    #print ("var_one, the datetime trigger is     ",var_one)
    
print ("total rows pulled from db is     ", total_count)
print ("                           end                             ")


   

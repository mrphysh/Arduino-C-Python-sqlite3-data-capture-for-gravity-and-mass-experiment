import sqlite3   
import datetime
from datetime import datetime,timedelta
conn = sqlite3.connect('feb_pract__database_partial')      # one table only 'first_table'
c = conn.cursor()


                   
c.execute("CREATE TABLE IF NOT EXISTS summary__table_two (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():

    c.execute("INSERT INTO summary__table_two(column_one,column_two,column_three,column_four) VALUES (?,?,?,?)",
		 ( date_var, col_two_avg  , col_thr_avg  ,  col_for_avg  ) )
    conn.commit()

date_var = '2020-02-21 12:00:00'#      
search_number = 500

print()
var_one = 34 # need something here
print()
number = 0
total_count = 0
num_added_db = 0
print ("++++++++++++++++++++++++++")
while (var_one  ):
    
    var_one = None                  #this needs to null  ..  will it be reset?
    c.execute ("SELECT column_one,column_five FROM first_table WHERE column_one > '%s'" %date_var)
    
    number =0                      
    
    col_two_sum   = 0              
    col_two_count = 0
    
    col_thr_sum   = 0
    col_thr_count = 0
    col_for_sum   = 0
    col_for_count = 0
  
    for row in c.fetchmany(search_number):
####        print (row[0])
####        print (row[1])
        five_var = (row[1])
        #print ("column_five is type", (type(five_var)))
        #five_var = int(five_var)
        #print (type(row[1])) #       five_var = int(five_var)
        #print ("it is changed to   ",type(five_var))
       
        var_one = row[0]         
        if five_var!= None:
            five_var = int(five_var)
            if ((five_var)>1750000.0  and (five_var)< 1804000.0):
                col_two_sum = col_two_sum + five_var
                col_two_count= col_two_count +1
            if ((five_var)>1804000  and (five_var)< 1821000):
                col_thr_sum = col_thr_sum + five_var
                col_thr_count= col_thr_count +1
            if ((five_var)>1821000  and (five_var)< 1895000):
                col_for_sum = col_for_sum + five_var
                col_for_count= col_for_count +1
        
        number = number +1
        
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
    
 
    if (col_two_sum > 1800000 and col_two_sum != None):
        
        col_two_avg = int(col_two_sum/(col_two_count ))
    else:
        col_two_avg = None
       
    if (col_thr_sum > 1800000 and col_thr_sum != None):
        ######  this is not  calculating correctly
        col_thr_avg = int(col_thr_sum/(col_thr_count ))
    else:
        col_thr_avg = None
       # print ("          the average for col_thr for this day is ",  col_thr_avg)
    if (col_for_sum > 1800000 and col_for_sum !=None):  #  is null less than 1500000?
                                                        #  this is not causing problems, but not helping
        
        col_for_avg = int(col_for_sum/(col_for_count ))
    else:
        col_for_avg = None
       
 
    dynamic_data_entry_averages()    
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("                           end                             ")


   

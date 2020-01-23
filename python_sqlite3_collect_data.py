import sqlite3   
import datetime
from datetime import datetime,timedelta
#
database =  "017_jan08_2020_db_no_sort"
receiving_database = "summary_database"
#
conn = sqlite3.connect(database)      # one table only 'first_table'
c = conn.cursor()
#
conn_2 = sqlite3.connect(receiving_database)
c_2 = conn_2.cursor()
#
c_2.execute("CREATE TABLE IF NOT EXISTS summary_for_real (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five text,column_six REAL )") 
print ("++++++++++++++++++")
print (database)
#
def dynamic_data_entry_averages():
    conn_2.execute("INSERT INTO summary(column_one,column_two,column_three,column_four, column_five,column_six) VALUES (?,?,?,?,?,?)",( date_var, col_two_avg  , col_thr_avg  ,  col_for_avg ,database,number_for_db ) )
    conn_2.commit()
#
date_var = '2020-01-08'#      
search_number = 150

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%  tell them apart  %%%%%%%%%%%%%%%%")
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
##        print (row[0])
##        print (row[1])
        five_var = (row[1])
       # print (type(row[1]))
        #five_var = int(five_var)
       # print (type(five_var))
        var_one = row[0]         
        if five_var!= None:
            if ((five_var)>1800000  and (five_var)< 1818500):
                col_two_sum = col_two_sum + five_var
                col_two_count= col_two_count +1
            if ((five_var)>1818500  and (five_var)< 1824000):
                col_thr_sum = col_thr_sum + five_var
                col_thr_count= col_thr_count +1
            if ((five_var)>1824000  and (five_var)< 1895000):
                col_for_sum = col_for_sum + five_var
                col_for_count= col_for_count +1
        
        number = number +1
        
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number_for_db = number
    number = 0  #  this needs to be reset
    
    date = datetime.strptime(date_var, "%Y-%m-%d")  # this sets up the variable for altering
    new_date = date + timedelta(days = 1)     # new_date is created here to accept the next day?
    #datetime.strftime(new_date, "%Y-%m-%d")  # the object is turned back into a string  no??
    date_var = str(new_date)
    date_var = date_var[0:10]
 
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
   # print("date   ",date_var,"  ",col_two_avg,"  ", col_thr_avg,"  ",  col_for_avg)
   # print ("type date_var   ",(type(date_var)))
    dynamic_data_entry_averages()    
    
    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")


   

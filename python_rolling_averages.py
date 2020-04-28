import sqlite3   
import datetime
from datetime import datetime,timedelta
conn = sqlite3.connect('jan08_2020_db_no_sort')      # one table only 'first_table'
c = conn.cursor()

                   
c.execute("CREATE TABLE IF NOT EXISTS summary_rolling_two (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    c.execute("INSERT INTO summary_rolling_two(column_one,column_two,column_three,column_four) VALUES (?,?,?,?)",( date_var, col_two_avg  , col_thr_avg  ,  col_for_avg  ) )
    conn.commit()
def dynamic_data_entry_averages_mu():
    c.execute("INSERT INTO summary_col_for(column_one,column_four) VALUES (?,?)",( date_var,   col_for_avg  ) )
    conn.commit()
    
date_var = '2020-01-08 12:00:00'#
low_value = 1814
mid_value  = 1823
high_value  =  1936
window      = 200  #  and this is apples and oranges example 1870000 plus or minus 400

search_number = 3000

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
##        print (row[0])
##        print (row[1])
        
        #print (type(row[1]))
        five_var = (row[1])
       # print (type(five_var))
        var_one = row[0]         
        if five_var!= None:
            five_var = int(five_var)
            if ((five_var)>(low_value*1000)- window  and (five_var)< ((low_value*1000)+window)):
                col_two_sum = col_two_sum + five_var
                col_two_count= col_two_count +1
            if ((five_var)>(mid_value*1000)- window  and (five_var)< ((mid_value*1000)+window)):
                col_thr_sum = col_thr_sum + five_var
                col_thr_count= col_thr_count +1
            if ((five_var)>(high_value*1000)- window  and (five_var)< ((high_value*1000)+window)):
                col_for_sum = col_for_sum + five_var
                col_for_count= col_for_count +1
        
        number = number +1
    
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
 
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
        ################################
    print("date   ",date_var,"  ",col_two_avg,"    ", col_thr_avg,"     ",  col_for_avg)
    print ("the windows are,repectively   ",low_value,"  ",mid_value,"  ", high_value )
    dynamic_data_entry_averages() 
    if col_two_avg  != None :
        low_value  = int(col_two_avg/1000) 
    
    if col_thr_avg != None:
        mid_value = int(col_thr_avg/1000) 
    
    if col_for_avg != None:
        high_value = int(col_for_avg/1000)
    
    print ()
       
    #dynamic_data_entry_averages_mu()    
    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")


   

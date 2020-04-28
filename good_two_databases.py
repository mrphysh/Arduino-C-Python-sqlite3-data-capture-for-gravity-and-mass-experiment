import sqlite3   
import datetime
from datetime import datetime,timedelta
"""
this script is for development.  From the string of numbers, this script picks out
one set of number.  This is among as amny as six sets.
I use DBBrowser to look at the databases; works great.

"""

conn = sqlite3.connect('mar14_par_four')      # one table only 'first_table'
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS summary_rolling_two (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )")


bonn = sqlite3.connect('summ_march_pract_two')      # one table only 'first_table'
b = bonn.cursor()
b.execute("CREATE TABLE IF NOT EXISTS summary_one (column_one TEXT,column_two REAL,column_three REAL, column_four REAL, column_five REAL,column_six REAL )") 




print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    b.execute("INSERT INTO summary_one(column_one,column_two) VALUES (?,?)",( date_var, col_two_avg   ) )
    bonn.commit()
    
date_var = '2020-03-14 12:00:00'#
low_value = 1878
print ("low_val is of type",type(low_value))

window      = 2000  #  and this is apples and oranges example 1870000 plus or minus 400

search_number = 3000

print()
var_one = 34 # need something here
print()
number = 0
total_count = 0
num_added_db = 0
print ("++++++++++++++++++++++++++")
while (var_one ):
    
    
    c.execute ("SELECT column_one,column_five FROM first_table WHERE column_one > '%s'" %date_var)
    var_one = None                  #this needs to null  ..  will it be reset?
    number =0                      
    
    col_two_sum   = 0              
    col_two_count = 0
    
   
  
    for row in c.fetchmany(search_number):

     
        holder = (row[1])
        
       
        var_one = row[0]         
        if holder!= None:
            five_var = int(holder)
            
            
            if ((five_var)>(low_value*1000)- window  and (five_var)< ((low_value*1000)+window)):
                col_two_sum = col_two_sum + five_var
                col_two_count= col_two_count +1
            
        
        number = number +1
    
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
    
 
    if (col_two_sum > 1800000 and col_two_sum != None):
        
        col_two_avg = int(col_two_sum/(col_two_count ))
    else:
        col_two_avg = None
       
   
        ################################
    print ("five_var type is    ",type(five_var))
    print("date   ",date_var,"                      ",col_two_avg)
    print ("the average is   ",low_value  )
    dynamic_data_entry_averages() 
    if col_two_avg  != None :
        low_value  = (col_two_avg/1000) 
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
   
    print ()
       
    
    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")


   


import sqlite3   
import datetime
from datetime import datetime,timedelta
import sys
import os
script_name = os.path.basename(sys.argv[0])
print (script_name)
##                                              this is DATACOLLECTED/dev_prototype_02.py
data_source_database = "008_april_19_2019_db_no_sort"
##
summary_database = "my_database"
##
summary_table =  "summary"###this is not working
for_database = script_name + "   " + data_source_database  ## put both fields together for the database
print (for_database)
##
conn = sqlite3.connect(data_source_database)      # one table only 'first_table'
c = conn.cursor()

#bonn = sqlite3.connect(summary_database)      # one table only 'first_table'
#b = bonn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS summary_table_two (column_zero TEXT  ,  column_one REAL, column_two REAL,column_three REAL, column_four REAL,\
        column_five REAL,column_six REAL,column_seven REAL, column_eight REAL, column_nine REAL,column_ten REAL,column_eleven REAL, column_twelve REAL, \
        column_thirteen REAL , column_fourteen REAL,column_fifteen TEXT )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    c.execute("INSERT INTO summary_table_two(column_zero,column_one,column_two,column_three,column_four,\
    column_five,column_six,column_seven,column_eight,column_nine,column_ten,column_eleven,column_twelve,column_thirteen,column_fourteen,column_fifteen)\
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",( date_var,one_average,two_average,thr_average,for_average,five_average,six_average,no_val,\
                                                row_count,one_count,two_count,thr_count,for_count,five_count,six_count, for_database  ) )
    conn.commit()
##
##    
date_var = '2019-04-19 12:00:00'#
one_target = 1810
two_target  = 1819
thr_target  =  1829

for_target = 189
five_target = 120
six_target = 187
#
window      = 1500  #  and this is apples and oranges example 1870000 plus or minus 400
#
search_number =  40
#
print()
var_one = 34 # need something here.  Does the search find a value?  this cannot be avoided
print()
number = 0
total_count = 0
num_added_db = 0
print ("++++++++++++++++++++++++++")
while (var_one  ):
    
    var_one = None                  #this needs to null  ..  will it be reset?
    c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %date_var)
    
    number =0  ;    no_val = 0; one_sum   = 0;one_count = 0
    
    two_sum = 0;two_count = 0;thr_sum   = 0;thr_count = 0
    
    for_sum = 0;for_count = 0;five_sum   = 0;five_count = 0;six_sum   = 0;six_count = 0
      
    one_average = 0;two_average = 0;thr_average = 0;for_average = 0;five_average=0;six_average = 0
   
    for row in c.fetchmany(search_number):
        var_one = row[0]  #  this is the time stamp
       # test_var = (row[1])
       # hold_var = 1000
        if row[1] != None:
            hold_var = int(row[1])
            
        if row[2] != None:
            hold_var = int(row[2]) 
        if row[3] != None:
            hold_var = int(row[3]) 
        if row[4] != None:
            hold_var = int(row[4])
        else:
            break                   #sometimes the row is blank
##        if row[5] != None:
##            hold_var = int(row[4]) # the python start is hanging it up
        #hold_var = row[1]+row[2]+row[3]+row[4]
        #
       
        #hold_var =  row[1]
        #print (hold_var)          #####      AT THSI POINT, THE PROGRAM IS WORKING!!!!!!!!!!!!!!!!
        if hold_var!= None:
           
            if ((hold_var)>(one_target*1000)- window  and (hold_var)< ((one_target*1000)+window)):
                one_sum = one_sum + hold_var
                one_count= one_count +1
            if ((hold_var)>(two_target*1000)- window  and (hold_var)< ((two_target*1000)+window)):
                two_sum = two_sum + hold_var
                two_count= two_count +1
            if ((hold_var)>(thr_target*1000)- window  and (hold_var)< ((thr_target*1000)+window)):
                thr_sum = thr_sum + hold_var
                thr_count= thr_count +1
            if ((hold_var)>(for_target*1000)- window  and (hold_var)< ((for_target*1000)+window)):
                for_sum = for_sum + hold_var
                for_count= for_count +1
            if ((hold_var)>(five_target*1000)- window  and (hold_var)< ((five_target*1000)+window)):
                five_sum = five_sum + hold_var
                five_count= five_count +1
            if ((hold_var)>(six_target*1000)- window  and (hold_var)< ((six_target*1000)+window)):
                six_sum = six_sum + hold_var
                six_count= six_count +1
        
        number = number +1
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0  #  this needs to be reset
    
    if (one_sum > 1700000 and one_sum != None):
        
        one_average = int(one_sum/(one_count ))
    else:
        one_average = None
       
    if (two_sum > 1800000 and two_sum != None):
    
        two_average = int(two_sum/(two_count ))
    else:
        two_average = None
       
    if (thr_sum > 1700000 and thr_sum !=None):  #  is null less than 1500000?
                                                        #  this is not causing problems, but not helping
        
        thr_average = int(thr_sum/(thr_count ))
    else:
        thr_average = None

    if (for_sum > 1700000 and for_sum != None):
        
        for_average = int(for_sum/(for_count ))
    else:
        for_average = None
       
    if (five_sum > 1700000 and five_sum != None):
       
        five_average = int(five_sum/(five_count ))
    else:
        five_average = None
       # print ("          the average for col_thr for this day is ",  two_average)
    if (six_sum > 1700000 and six_sum !=None):  #  is null less than 1500000?
                                                        #  this is not causing problems, but not helping
        
        six_average = int(six_sum/(six_count ))
    else:
        six_average = None
        ################################
    row_count = one_count + two_count + thr_count +  for_count +  five_count + six_count
    print("date   ",date_var,"  ",one_average,"   ", two_average,"  ",  thr_average,"      ",for_average,"    ",five_average,"   ",six_average)
    print ("the targets are,repectively   ",one_target,"  ",two_target,"      ", thr_target,"        ",for_target,"         ",five_target,"        ",six_target )
    print ("row count...total of all counts    ", row_count)

    dynamic_data_entry_averages() 
    if one_average  != None :
        one_target  = int(one_average/1000)
             
    if two_average != None:
        two_target = int(two_average/1000) 
    
    if thr_average != None:
        thr_target = int(thr_average/1000)
    if for_average  != None :
        for_target  = int(for_average/1000)
             
    
    if five_average != None:
        five_target = int(five_average/1000) 
    
    if six_average != None:
        six_target = int(six_average/1000)
        
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
    
    print ()
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")


   

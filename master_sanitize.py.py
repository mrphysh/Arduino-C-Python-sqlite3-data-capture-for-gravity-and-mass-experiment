import sqlite3    #  just this library                          

conn = sqlite3.connect('test_database')      # one table only 'first_table'
c = conn.cursor()


time_variable = '2019-03-05 '                
'''
    This is a pretty good start.  I wanted to take the empty field and assign a variable and then make them 0
    That is lame.  just:: if row([3]):  'null' is a no
'''
c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %time_variable)#  I found this code and it seems to work fine.

for row in c.fetchmany(10):
    print (" ")
    print (" ")
    print ("space  space   space, ")
    column_one = (row[0])
    column_two =  (row[1 ])
    column_three = (row[ 2])
    column_four =  (row[ 3])
    column_five =  (row[ 4])
    column_six  = (row[5])
   

    
    if (row[0]):                 #actually, this column is always true... every row has a datetime stamp
        print ("datetime")
    else:
        column_one = 0
        
    if (row[1]):               #  the null value is an empty box, so returns a negative
        print ("row1")  
    else:
        column_two = 0          # replace the null with an int zero
        
    if (row[2]):
        print ("row2")  ###   does the variable exist?
    else:
        column_three = 0

    if (row[3]):
         print ("row3")
    else:
        column_four = 0
        
    if (row[4]):
        print ("row4")  
    else:
        column_five = 0
        
    if (row[5]):
        print ("row5")  ###   does the variable exist?
    else:
        column_six = 0
    print ("column_onr  =    ", column_one)
    print ("column_two  =    ", column_two)
    print ("column_three  =    ", column_three)
    print ("column_four  =    ", column_four)
    print ("column_five  =    ", column_five)
    print ("column_six  =    ", column_six)
  






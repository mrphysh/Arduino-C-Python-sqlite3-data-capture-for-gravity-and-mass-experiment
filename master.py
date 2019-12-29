import sqlite3    #  just this library                          

conn = sqlite3.connect('test_database')      # one table only 'first_table'
c = conn.cursor()


time_variable = '2019-03-10 '                
c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %time_variable)
number = 0  # initialize counter for lfetch loop
for row in c.fetchmany(8):#  this line brings in row after row
    print (row )
    print (row[0 ])  # this is just noise for development
    print (row[1 ])
    print (row[ 2])
    print (row[ 3])
    print (row[ 4])
    number = number +1

print (number)  











import sqlite3    #  just this library                          

conn = sqlite3.connect('test_database')      # one table only 'first_table'
c = conn.cursor()


time_variable = '2019-03-10 '                
'''
     #  this variable is an important point of control
                    #  for this prototype, let's not worry about operator input
                    #   This is string, but the Python seems to accept
                    #  it against a ">"   operation
'''
c.execute ("SELECT * FROM first_table WHERE column_one > '%s'" %time_variable)#  I found this code and it seems to work fine.
number = 0  # initialize counter for lfetch loop
for row in c.fetchmany(8):#  this line brings in row after row
    #up to 8 in this case
    #a day is about 7000 rows
    # so it would be fetchmany(6000)
    #
    #
    #   the data needs to sanitized (I checked the meaning and it is correct "sanitized")
    #        NotNull  these need to be changed to integer 0
    #    no alpha numeric characters, no strings, just numbers as integers
    #  the data is inherently quite precise,  Outliers need to be ommitted.  See Readme.
    #  I assume that this should be a function and even a library module.
    #  
    # every c.execute ("SELECT .....") generates one data point plus the date time stamp.
    # So SELECT and fetch (6000)  one point
    # next 6000      one point
    #  next 6000     one point
    # etc,  this is the approach toward summarizing the 3 million rows.
    print (row )
    print (row[0 ])  # this is just noise for development
    print (row[1 ])
    print (row[ 2])
    print (row[ 3])
    print (row[ 4])
    number = number +1
    ##Accumulate data for statistical analysis.  I assume that this means pushing the numbers into a list
    ##There is one number per row.  This could be treated as a flat file.  Add column_two,column_three,column_four and
    ##column_five.  Push that value into a list. (maybe do a sanity check.  how about a sanitized check)

print (number)  # this just shows the number of lines
#  now the 6000 numbers are in a list.  We ned an average and standard deviation.  Should be easy with Pandas
#  then put the time stamp average and Stdev in the new database
#  move to the next day and do it again.
#  The result would go in a different database altogether,
#  requiring a different connection object and cursor object.   I have never done that but it should be 'no big deal'.

# so we would need all this in a loop, incremented by one day.  As mentioned in the Readme, a trick might be to
#  increment the day and do SELECT * WHERE time_var > day_variable
#          followed by       fetchmany(6000)
#we are looking for a global picture of the 3 million numbers and fine attention to detail may be unimportant.
####      also, the commments need to be properly indented or the compiler gives an error.  I am getting better.













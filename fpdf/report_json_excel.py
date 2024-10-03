# pip install xlsxwriter 
# https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/

import xlsxwriter
 
# Workbook() takes one, non-optional, argument 
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')
 
# The workbook object is then used to add new 
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet("Sheet1")
 
# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
# worksheet.write('C1', 'For')
# worksheet.write('D1', 'Geeks')
 
row = 1
column  = 0

content1 = ["1", "1", "2", "2",
                    "3", "5", "7"]

content2 = ["5", "2", "6", "8",
                    "6", "4", "6"]
for item in content1 :
 
    # write operation perform
    worksheet.write(row, column, item)
 
    # incrementing the value of row by one
    # with each iterations.
    row += 1

row = 1
column  = 1
for item in content2 :
 
    # write operation perform
    worksheet.write(row, column, item)
 
    # incrementing the value of row by one
    # with each iterations.
    row += 1


# Finally, close the Excel file
# via the close() method.
workbook.close()

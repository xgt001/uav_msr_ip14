__author__ = 'ganesh'

import xlwt

sheet = xlwt.Workbook()

# Sheet Name
char_sheet = sheet.add_sheet("Target Details")


#Fill the Column Titles
char_sheet.write(0,0,"Shape Detected")

char_sheet.write(0,1,"Shape Color")

char_sheet.write(0,2,"Character Detected")

char_sheet.write(0,3,"Character Color")

char_sheet.write(0,4,"Latitude")

char_sheet.write(0,5,"Longitude")

char_sheet.write(0,6,"Orientation")

for i in range(0,7,1):
    print i
    char_sheet.col(i).width = 5120


sheet.save("blob.xls")







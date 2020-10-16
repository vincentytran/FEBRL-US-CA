# Author: Vincent Tran (vincent@imt.ca)
# Format the output to look like a proper csv file.

fileOut = open('dsg2500.csv', 'w')

fileIn = open('ds500.csv', 'r')
count = 0
line = fileIn.readline()  # skip header
sep = ','
recordIdPrefix = 'A'

fileOut.write('RECORD_ID' + sep +
              'NAME_LAST' + sep + 
              'NAME_FIRST' + sep + 
              'NAME_PREFIX' + sep + 
              'GENDER' + sep + 
              'DATE_OF_BIRTH' + sep + 
              'SSN_NUMBER' + sep + 
              'HOME_ADDR_LINE1' + sep + 
              'HOME_ADDR_LINE2' + sep + 
              'HOME_ADDR_CITY' + sep + 
              'HOME_ADDR_STATE' + sep + 
              'HOME_ADDR_POSTAL_CODE' + sep + 
              'PHONE_NUMBER' + "\n"
              )
while True:
    count += 1

    line = fileIn.readline()
    if not line:
        break

    data = line.upper().split(",")
    if len(data) > 10:
        fileOut.write(recordIdPrefix + (data[0]).strip() + sep +
            (data[8]).strip() + sep +
            (data[7]).strip() + sep +
            (data[6]).strip() + sep +
            (data[3]).strip() + sep +
            (data[5]).strip() + sep +
            (data[16]).strip() + sep +
            ((data[12]).strip() + ' ' + (data[13]).strip()).strip() + sep +
            (data[14]).strip() + sep +
            (data[10]).strip() + sep +
            (data[9]).strip() + sep +
            (data[11]).strip() + sep +
            (data[15]).strip() + "\n"
            )
fileIn.close()
fileOut.close()


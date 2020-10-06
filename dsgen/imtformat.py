# Author: Vincent Tran (vincent@imt.ca)
# Format the output to look like a proper csv file.

fileOut = open('imt1000.csv', 'w')

fileIn = open('dataset1000.csv', 'r')
count = 0
line = fileIn.readline()  # skip header
sep = '|'

fileOut.write('id' + sep +
              'onmlast' + sep + 
              'onmfirst' + sep + 
              'onmtitle' + sep + 
              'gender' + sep + 
              'dob' + sep + 
              'ssn' + sep + 
              'stline1' + sep + 
              'stline2' + sep + 
              'city' + sep + 
              'state' + sep + 
              'zipcode' + sep + 
              'phone' + sep + "\n"
              )
while True:
    count += 1

    line = fileIn.readline()
    if not line:
        break

    data = line.split(",")
    fileOut.write((data[0]).strip() + sep +
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
                  (data[15]).strip() + sep + "\n"
                  )
fileIn.close()
fileOut.close()


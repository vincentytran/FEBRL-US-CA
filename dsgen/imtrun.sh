# Author: Vincent Tran (vincent@imt.ca)
# Example on how to run generate2.py

python generate2.py dataset1000.csv 1000 1000 2 2 2 uniform all 50 > dataset1000.info.txt
python generate2.py dataset10000.csv 10000 10000 2 2 2 uniform all 500 > dataset10000.info.txt

c:\Python27\python.exe generate2.py ds500.csv 500 500 5 5 5 uniform all 100 > ds500.info.txt
c:\Python27\python.exe imtformat2.py
import csv

customers = open('customers.csv','r')
#infile = open('customer_country.csv')

csv_file = csv.reader(customers)

#to skip the header and start on the next lone
next(csv_file)
num = 0
outfile = open('customer_country.csv', 'w')
outfile.write('Full Name, Country'+'\n')
for rec in csv_file:    #This brings each record into a list format
    #print (rec) 
    num +=1
    outfile.write(f'{rec [1]} {rec [2]}, {rec [4]}' + '\n')
print(f'Total Customers: {num}')


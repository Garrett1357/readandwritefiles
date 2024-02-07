import csv
employee = open('employee_data.csv','r')
csv_file = csv.reader(employee)
#to skip the header and start on the next lone
next(csv_file)
for rec in csv_file:    #This brings each record into a list format
    #print (rec) 
    salary = int(rec [3])
    bonus = float(rec [7])
    total_bonus= (salary * bonus)
    total = salary + total_bonus
    print(f"Name:   {rec[1]}")
    print(f'Salary: ${salary}')
    print(f'Bonus:  ${total_bonus}')
    print(f'Pay:    ${total}')
    input()
working_hours = input("Enter the hours worked: ")
wage = int(input("Enter hourly wage: "))

working_hours = working_hours.split()

week_hours = [int(x) for x in working_hours]

total_hrs = sum(week_hours)

if total_hrs <= 40:
    total_wages = total_hrs * wage
else:
    overtime = total_hrs - 40
    total_wages = 40 * wage + overtime * wage * 1.5

print('Total Wages: ', total_wages)

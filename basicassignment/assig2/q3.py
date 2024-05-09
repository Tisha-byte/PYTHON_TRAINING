employee_id=int(input("enter employ ID:"))
working_hrs=int(input("enter working hours:"))
salary_amt=float(input("enter the salary amount per hour:"))
print(employee_id)
salary=working_hrs*salary_amt
print(round(salary,3))
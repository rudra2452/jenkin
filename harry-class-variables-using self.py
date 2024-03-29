class employee:
    increment=1.5
    increment1=1.25
    number_of_employee=0
    def __init__(self, fname, lname, salary):
        self.lname=lname
        self.fname=fname
        self.salary=int(salary)
        employee.number_of_employee +=1
    def increase(self): 
        self.salary= int(self.salary * employee.increment)
    def increase1(self):
        self.salary= int(self.salary * employee.increment1)
    
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True
print(employee.isopen("sunday"))
print(employee.number_of_employee)
    

prem=employee('prem','prakash','250000')
print(employee.number_of_employee)
rohan=employee('rohan','das','450000')
print(employee.number_of_employee)
print(prem.salary)
prem.increase()
print(prem.salary)
print(prem.__dict__)
print(rohan.salary)
rohan.increase1()
print(rohan.salary)

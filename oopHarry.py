#class employee():
    #pass
#prem= employee()
#rohan= employee()

#prem.fname= "prem"
#prem.lname="prakash"
#prem.salary="250000"
#rohan.fname="rohan"
#rohan.lname="das"
#rohan.salary="50000"
#print(prem.salary) # This is an example of simple program and in case of large number of employees, it will be difficult to mention all details.
#please see how we can shorten it

class employee:
    def __init__(self, fname, lname, salary):
        self.lname=lname
        self.fname=fname
        self.salary=salary
    
prem=employee('prem','prakash','250000')
rohan=employee('rohan','das','450000')
print(prem.salary,rohan.salary);
print(prem.fname, rohan.fname)

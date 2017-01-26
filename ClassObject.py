class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+= 1

    def displyCount(self):
        print("Total Employee %d" %Employee.empcount)

    def displayEmployee(self):
        print("Name : ",self.name, ",Salary:", self.salary)
              


#this would creat first object of employee class
emp1 = Employee("Zara",2000)
#this would create second object of employee class
emp2=Employee("Manii",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print( "Total employee %d" % Employee.empcount)
emp1.age=7
emp2.age=8
if hasattr(emp1,'age'):
    print("the attribut age exists")
getattr(emp1,'age')
setattr(emp1,'age',8)
              
            

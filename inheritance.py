class Person:
    def person_info(self, name, age):
        print("Inside person class")
        self.name=name
        print('Name:',name,'Age:',age)

class Company:
    def company_info(self, company_name, locaton):
        print("Inside company class")
        print('Company Name:',company_name,'Location:',location)
    
class Employee(Person, Company):
    def employee_info(self,salary,skill):
        super().person_info('Binod',20)
        print('Inside Employee Class')
        print('Salary:',salary,'Skill:',skill)

emp=Employee()
emp.person_info('Jessi',28)
emp.employee_info(1200, 'Machine')
    
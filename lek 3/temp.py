class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.emp_count)  
  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))


emp1 = Employee("Андрей", 2000)  
emp2 = Employee("Мария", 5000)

emp1.display_employee()  
emp2.display_employee()  

emp1.display_count()
#print("Всего сотрудников: %d" % Employee.emp_count)
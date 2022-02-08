#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Emmanuel Paul-chinka
#100823134

################################### QUESTION 1 #################################


class Person:
    def __init__(self, first_name, last_name, age, address, contact_number) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.contact_number = contact_number


class Employee(Person):
    def __init__(self, first_name, last_name, age, address, contact_number, employee_id, organization_name, position) -> None:
        
        super().__init__(first_name, last_name, age, address, contact_number)

        self.employee_id = employee_id
        self.organization_name = organization_name
        self.position = position


class CommisionEmployee(Employee):
    def __init__(self, first_name, last_name, age, address, contact_number, employee_id, organization_name, position, commission_rate) -> None:
        super().__init__(first_name, last_name, age, address, contact_number, employee_id, organization_name, position)


        self.commision_rate = commission_rate

 
        self.total_earnings = 0

 
    def calculate_commission(self):
        sales = float(input("Please Enter Gross Sales... : "))

        self.total_earnings = sales * self.commision_rate

 
    def display_data(self):
        print(f'first name: {self.first_name}, last name: {self.last_name}, age: {self.age}, address: {self.address}, contact number: {self.contact_number}, employee id: {self.employee_id}, organization name: {self.organization_name}, position: {self.position}, commission rate: {self.commision_rate}, total earnings: {self.total_earnings}')


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, age, address, contact_number, employee_id, organization_name, position, base_salary) -> None:
        super().__init__(first_name, last_name, age, address, contact_number, employee_id, organization_name, position)

        self.base_salary = base_salary

 
    def calculate_net_salary(self):
        net_salary = self.base_salary
        net_salary -= net_salary * .13
        net_salary -= net_salary * .1
        net_salary -= net_salary * .3

        print(f"Net salary: {net_salary}")


class BasePlusCommissionEmployee(CommisionEmployee):    
    def __init__(self, first_name, last_name, age, address, contact_number, employee_id, organization_name, position, commission_rate, base_salary) -> None:
        
        super().__init__(first_name, last_name, age, address, contact_number, employee_id, organization_name, position, commission_rate)
        self.base_salary = base_salary


    def calculate_total_earnings(self):
        self.total_earnings = super().calculate_commission() + self.base_salary

  
    def display_data(self):
        print(f'first name: {self.first_name}, last name: {self.last_name}, age: {self.age}, address: {self.address}, contact number: {self.contact_number}, employee id: {self.employee_id}, organization name: {self.organization_name}, position: {self.position}, total earnings: {self.total_earnings()}')


# In[ ]:





# In[ ]:





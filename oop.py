class Department:
    list_of_managers = []
    POSITIONS = {'developer', 'designer', 'manager'}
    team_list = {}

    def get_salary(self):
        pass


class Employee(Department):
    employee_id = 0

    def __init__(self, first_name, second_name, salary, experience, team_id):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.team_id = team_id
        self.employee_id += 1

    def get_salary(self):
        if self.experience > 2:
            self.salary += 200
        if self.experience > 5:
            self.salary = (self.salary*1.2)+500
        return self.salary

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


class Developer(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id, eff_coefficient):
        super().__init__(first_name, second_name, salary, experience, team_id)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)

class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id, eff_coefficient):
        super().__init__(first_name, second_name, salary, experience, team_id)
        self.eff_coefficient = eff_coefficient

    def get_salary(self):
        return Employee.get_salary(self) * self.eff_coefficient

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id):
        super().__init__(first_name, second_name, salary, experience, team_id)

    def getSalary(self):
        if len(self.team_list) > 5:
            self.salary + 200
        if len(self.team_list) > 10:
            self.salary + 300
            dev_count = 0
        for member in self.team_list:
            if member == 'developer':
                dev_count += 1
            if dev_count > len(self.team_list/2):
                self.salary = self.salary *1.1
        return self.salary

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)

d=Designer('Ivan','Ivanov', 100, 3, '3', 4)
print(d)
print(d.get_salary())

class Department:
    list_of_managers = []
    POSITIONS = {'developer', 'designer', 'manager'}
    team_list = {}

    def __init__(self, team_list):
        self.team_list = team_list

    def get_salary(self):
        pass

    def __str__(self):
        return "%s" % self.team_list


class Employee(Department):
    employee_id = 0

    def __init__(self, first_name, second_name, salary, experience, team_id, position):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.team_id = team_id
        self.position = position
        #self.position = Department.POSITIONS
        self.employee_id += 1

    def add_to_team(self):
        # team_id -> position -> firstName,secondName
#         for team_id, position, name in Department.team_list:
#             Department.team_list[team_id].append(self.team_id)
#             Department.team_list[position].append(self.position)
#             Department.team_list[name].append(self.first_name + ' ' + self.second_name)
# #        print(Department.team_list)
        Department.team_list = ({'team_id': self.team_id, 'position': self.position, 'name': self.first_name + ' ' + self.second_name})



    def get_salary(self):
        if self.experience > 2:
            self.salary += 200
        if self.experience > 5:
            self.salary = (self.salary*1.2)+500
        return self.salary

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


class Developer(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id, position='dev'):
        super().__init__(first_name, second_name, salary, experience, team_id, position)

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id, eff_coefficient, position='des'):
        super().__init__(first_name, second_name, salary, experience, team_id, position)
        self.eff_coefficient = eff_coefficient

    def get_salary(self):
        return Employee.get_salary(self) * self.eff_coefficient

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experience, team_id, position='man'):
        super().__init__(first_name, second_name, salary, experience, team_id, position)

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


d=Designer('Ivan','Ivanov', salary=100, experience=3, team_id=11, eff_coefficient=4)
d.add_to_team()
m=Manager('Petr','Petrov', salary=100, experience=3, team_id=11)
m.add_to_team()
print(d)
print(d.get_salary())
print(Department.team_list)

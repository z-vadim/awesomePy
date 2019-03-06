class Department:
    team_list = {}

    def __init__(self, team_list):
        self.team_list = team_list()

    def get_salary(self):
        pass

    def __str__(self):
        return "%s" % self.team_list


class Employee(Department):

    def __init__(self, first_name, second_name, salary, experience, team_id, position):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.team_id = team_id
        self.position = position

    def add_to_team(self):
        if self.team_id in self.team_list.keys():
            if self.position in Department.team_list[self.team_id][0]:
                Department.team_list[self.team_id][0].append([self.first_name + ' ' + self.second_name])
            else:
                Department.team_list[self.team_id].append([self.position, [self.first_name + ' ' + self.second_name]])
        else:
            Department.team_list[self.team_id] = [[self.position, [self.first_name + ' ' + self.second_name]]]

    def get_salary(self):
        if self.experience > 2:
            self.salary += 200
        if self.experience > 5:
            self.salary = (self.salary*1.2)+500
        return self.salary

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)

    def __repr__(self):
        return "%s %s, manager %s, experience %s" % (self.first_name, self.second_name, self.manager, self.experience)


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

    def get_salary(self):
        for x in Department.team_list[self.team_id]:
            if x[0] == 'des':
                if (len(x[0])-1) > 1:
                    self.salary += 200
                if (len(x[0])-1) > 10:
                    self.salary += 300
                if len(x[0])>len(x)/2:
                    print('lan -- %s' %len(x))
                    self.salary = int(self.salary*1.1)
        return self.salary

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.second_name, self.salary, self.experience)


d=Designer('Ivan','Ivanov', salary=100, experience=3, team_id=11, eff_coefficient=4)
d.add_to_team()
a=Designer('Ivan','Petrov', salary=100, experience=1, team_id=11, eff_coefficient=4)
a.add_to_team()
b=Designer('Petr','Ivanov', salary=100, experience=1, team_id=12, eff_coefficient=1)
b.add_to_team()
c=Developer('Ya','Ya', salary=100, experience=1, team_id=12)
c.add_to_team()
m=Manager('Petr','Petrov', salary=100, experience=3, team_id=11)
m.add_to_team()
print(d)
print(d.get_salary())
print(Department.team_list)
print(m)
print(m.get_salary())
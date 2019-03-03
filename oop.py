class Employee:
    employee_id = 0
    list_of_managers = []
    emp_position = {'developer', 'designer', 'manager'}
    team_list = []

    def __init__(self, first_name, second_name, salary, experience, eff_coefficient, is_manager, position):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.eff_coefficient = eff_coefficient
        self.is_manager = is_manager
        self.position = position
        self.team_id = team_id

        Employee.employee_id += 1

    def getSalary(self):

        if self.experience > 2:
            self.salary + 200
        elif self.experience > 5:
            self.salary = (self.salary*1.2)+500

        if self.position == "designer":
            self.salary = self.salary * self.eff_coefficient
        if self.position == "manager":
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

    def represent(self):
        return "%s %s: manager: %s" %(self.first_name, self.second_name, self.salary)
class Employee:
    def __init__(self, id, name, basic_salary):
        self.id = id
        self.name = name
        self.basic_salary = basic_salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_basic_salary(self):
        return self.basic_salary

    def __str__(self):
        return 'ID: {} - Name: {} - Salary: ${:.1f}'.format(
            self.id, self.name, self.basic_salary
        )


class Faculty(Employee):
    def __init__(self, id, name, basic_salary, degree, teaching_hours):
        super().__init__(id, name, basic_salary)
        self.degree = degree
        self.teaching_hours = teaching_hours

    def set_degree(self, degree):
        self.degree = degree

    def set_teaching_hours(self, teaching_hours):
        self.teaching_hours = teaching_hours

    def __str__(self):
        return 'ID: {} - Name: {} - Degree: {} - Teaching Hours: {} - Salary: ${:.1f}'.format(
            self.id, self.name, self.degree, self.teaching_hours, self.salary()
        )

    def salary(self):
        return self.basic_salary + self.teaching_hours * 100


class Staff(Employee):
    def __init__(self, id, name, basic_salary, job_title, working_hours):
        super().__init__(id, name, basic_salary)
        self.job_title = job_title
        self.working_hours = working_hours

    def get_job_title(self):
        return self.job_title

    def get_working_hours(self):
        return self.working_hours

    def __str__(self):
        return 'ID: {} - Name: {} - Job Title: {} - Working Hours: {} - Salary: ${:.1f}'.format(
            self.id, self.name, self.job_title, self.working_hours, self.salary()
        )

    def salary(self):
        if self.working_hours <= 8:
            return self.basic_salary
        else:
            return self.basic_salary * 1.25


if __name__ == '__main__':
    emp1 = Employee(1234, 'Anna', 1200)
    fc1 = Faculty(2222, 'Deni', 1200, 'PhD', 8)
    stf1 = Staff(81234, 'Sara', 1000, 'Registrar', 10)

    print(emp1)
    print(fc1)
    print(stf1)

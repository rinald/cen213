class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def to_string(self):
        print('Person name:', self.name)
        print('Birth Year:', self.birth_year)


class Student(Person):
    def __init__(self, name, birth_year, major):
        super().__init__(name, birth_year)
        self.major = major

    def to_string(self):
        print('Student name:', self.name)
        print('Birth Year:', self.birth_year)
        print('Major:', self.major)


class Instructor(Person):
    def __init__(self, name, birth_year, salary):
        super().__init__(name, birth_year)
        self.salary = salary

    def to_string(self):
        print('Instructor name:', self.name)
        print('Birth Year:', self.birth_year)
        print('Salary:', self.salary)


if __name__ == '__main__':
    person = Person('Keni', 1990)
    student = Student('Deni', 1980, 'Electronic Engineering')
    instructor = Instructor('Prof. Beni', 1979, 35000)

    for i in (person, student, instructor):
        i.to_string()
        print()
